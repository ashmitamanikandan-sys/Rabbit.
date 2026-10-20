"""Stream Open Library works dumps into RABBIT's existing Supabase books table.

Usage:
  python scripts/import_openlibrary_dump.py --file ol_dump_works_latest.txt.gz --max-records 50000
  python scripts/import_openlibrary_dump.py --file ol_dump_works_latest.txt.gz --max-records 0

Uses existing books schema; imports metadata as pending, NEVER fabricated chapter data.
Large runs should use a persistent worker with checkpointing, not a short GitHub Action.
"""
import argparse
import gzip
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = os.environ.get("SUPABASE_URL", "").rstrip("/")
KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")
BATCH_SIZE = 100
RETRY_CODES = {429, 500, 502, 503, 504}


def send(batch):
    if not batch:
        return
    endpoint = BASE + "/rest/v1/books?on_conflict=open_library_work_id"
    payload = json.dumps(batch, ensure_ascii=False).encode("utf-8")
    headers = {
        "apikey": KEY, "Authorization": "Bearer " + KEY,
        "Content-Type": "application/json",
        "Prefer": "resolution=ignore-duplicates,return=minimal",
    }
    for attempt in range(6):
        try:
            req = urllib.request.Request(endpoint, data=payload, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=90):
                return
        except urllib.error.HTTPError as error:
            if error.code not in RETRY_CODES or attempt == 5:
                raise RuntimeError("Supabase import failed: HTTP " + str(error.code) + " " +
                                   error.read(500).decode("utf-8", "replace")) from error
            time.sleep(min(2 ** attempt, 30))
        except urllib.error.URLError:
            if attempt == 5:
                raise
            time.sleep(min(2 ** attempt, 30))


def clean(value, max_length=500):
    return re.sub(r"\\s+", " ", str(value or "")).strip()[:max_length]


def work_record(record):
    key = record.get("key", "")
    if not re.fullmatch(r"/works/OL[0-9]+W", key):
        return None
    title = clean(record.get("title"))
    if not title:
        return None
    # Works dumps store author IDs, not author names. Do NOT invent an author.
    # The current books schema requires author; use a transparent placeholder.
    authors = record.get("authors") or []
    first = authors[0].get("author", {}).get("key", "") if isinstance(authors[0], dict) else ""
    author = "Author not yet resolved" if first else "Author unavailable"
    covers = record.get("covers") or []
    cover = next((n for n in covers if isinstance(n, int) and n > 0), None)
    return {
        "open_library_work_id": key,
        "title": title,
        "author": author,
        "cover_url": "https://covers.openlibrary.org/b/id/" + str(cover) + "-M.jpg" if cover else None,
        "catalog_status": "pending",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True, help="Local Open Library works dump (.txt or .gz)")
    parser.add_argument("--max-records", type=int, default=10000,
                        help="Maximum eligible works (0 means unlimited)")
    parser.add_argument("--skip-lines", type=int, default=0, help="Resume after this physical line")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if not args.dry_run and (not BASE.startswith("https://") or not KEY):
        parser.error("SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY are required")
    open_fn = gzip.open if args.file.endswith(".gz") else open
    batch, eligible, sent = [], 0, 0
    with open_fn(args.file, "rt", encoding="utf-8", errors="replace") as source:
        for line_number, line in enumerate(source, 1):
            if line_number <= args.skip_lines:
                continue
            try:
                # Open Library dump rows: type TAB key TAB revision TAB last_modified TAB JSON
                data = json.loads(line.rstrip("\\n").split("\\t", 4)[-1])
                item = work_record(data)
            except (ValueError, TypeError, IndexError, AttributeError):
                continue
            if not item:
                continue
            batch.append(item)
            eligible += 1
            if len(batch) >= BATCH_SIZE:
                if not args.dry_run:
                    send(batch)
                sent += len(batch)
                batch.clear()
                if sent % 10000 == 0:
                    print(json.dumps({"eligible": eligible, "processed": sent,
                                      "last_line": line_number}), flush=True)
            if args.max_records and eligible >= args.max_records:
                break
        if batch:
            if not args.dry_run:
                send(batch)
            sent += len(batch)
    print(json.dumps({"processed": sent, "dry_run": args.dry_run,
                      "last_line": line_number if 'line_number' in locals() else args.skip_lines,
                      "published": 0}), flush=True)


if __name__ == "__main__":
    main()
