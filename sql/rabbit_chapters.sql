-- RABBIT chapter-aware editorial schema.
-- Run in Supabase SQL editor after review. This file does NOT apply itself.
-- Bibliographic records are separate from original editorial work.
create table if not exists public.rabbit_chapter_outlines (
  id uuid primary key default gen_random_uuid(),
  book_id uuid not null references public.books(id) on delete cascade,
  chapter_number integer,
  chapter_title text not null,
  chapter_structure_status text not null default 'unverified'
    check (chapter_structure_status in ('verified','unverified','editorial_topic')),
  verification_source_url text,
  verification_notes text,
  display_order integer not null,
  created_at timestamptz not null default now(),
  unique (book_id, display_order),
  constraint verified_requires_source check (
    chapter_structure_status <> 'verified' or
    (verification_source_url is not null and length(trim(verification_source_url)) > 8)
  )
);
create table if not exists public.rabbit_chapter_summaries (
  id uuid primary key default gen_random_uuid(),
  outline_id uuid not null unique references public.rabbit_chapter_outlines(id) on delete cascade,
  preview text not null,
  full_explanation text not null,
  editorial_status text not null default 'draft'
    check (editorial_status in ('draft','review','published')),
  attribution text not null default 'Original RABBIT explanation; not book text',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  constraint preview_substantial check (length(trim(preview)) >= 300),
  constraint explanation_substantial check (length(trim(full_explanation)) >= 500)
);
create index if not exists rabbit_chapter_outlines_book_idx on public.rabbit_chapter_outlines(book_id,display_order);
create index if not exists rabbit_chapter_summaries_status_idx on public.rabbit_chapter_summaries(editorial_status);
alter table public.rabbit_chapter_outlines enable row level security;
alter table public.rabbit_chapter_summaries enable row level security;
drop policy if exists "Public read verified chapter outlines" on public.rabbit_chapter_outlines;
create policy "Public read verified chapter outlines" on public.rabbit_chapter_outlines
  for select to anon, authenticated using (
    exists (select 1 from public.rabbit_chapter_summaries s
      where s.outline_id=id and s.editorial_status='published')
  );
drop policy if exists "Public read published chapter summaries" on public.rabbit_chapter_summaries;
create policy "Public read published chapter summaries" on public.rabbit_chapter_summaries
  for select to anon, authenticated using (editorial_status='published');
-- Only trusted backend/service-role workflows should insert, edit, or publish.
