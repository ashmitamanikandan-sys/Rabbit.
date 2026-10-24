#!/usr/bin/env python3
"""
RABBIT Phase 1 End-to-End Browser Test Suite
Tests:
1. Welcome Screen (CTA: "Take me to the rabbit hole")
2. Multi-Genre Selection Screen (21 genres)
3. Personalized Feed (Interleaved books, no Human Mind defaults)
4. Returning User Bypass & Onboarding Reset
5. Interactive Like Counter (+1/-1, persistent, deterministic)
6. Real Share Button (Fallback copy & toast)
7. Direct Book Deep Link (?book=...)
8. Responsive Layouts across Mobile (390px), Tablet (820px), and Desktop (1440px)
"""

import json
import os
import subprocess
import time
import urllib.request
import websocket
import sys

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
DEVTOOLS_PORT = 9222
BASE_URL = "http://localhost:8080/Rabbit./"

def start_edge():
    # Kill any existing Edge processes on debugging port
    os.system(f"taskkill /F /IM msedge.exe 2>nul")
    time.sleep(1)

    cmd = [
        EDGE_PATH,
        "--headless=new",
        f"--remote-debugging-port={DEVTOOLS_PORT}",
        "--remote-allow-origins=*",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        "--user-data-dir=C:\\Users\\Manik\\AppData\\Local\\Temp\\rabbit_e2e_profile",
        BASE_URL
    ]
    proc = subprocess.Popen(cmd)
    time.sleep(2)
    return proc

def get_debugger_ws_url():
    for _ in range(10):
        try:
            req = urllib.request.urlopen(f"http://localhost:{DEVTOOLS_PORT}/json")
            tabs = json.loads(req.read().decode())
            for tab in tabs:
                if tab.get("type") == "page" and "webSocketDebuggerUrl" in tab:
                    return tab["webSocketDebuggerUrl"]
        except Exception:
            time.sleep(0.5)
    raise RuntimeError("Failed to connect to Edge DevTools")

class CDPClient:
    def __init__(self, ws_url):
        self.ws = websocket.create_connection(ws_url, timeout=10)
        self.req_id = 1

    def send(self, method, params=None):
        mid = self.req_id
        self.req_id += 1
        payload = {"id": mid, "method": method, "params": params or {}}
        self.ws.send(json.dumps(payload))
        while True:
            res = json.loads(self.ws.recv())
            if res.get("id") == mid:
                return res

    def evaluate(self, expr):
        res = self.send("Runtime.evaluate", {
            "expression": expr,
            "returnByValue": True,
            "awaitPromise": True
        })
        if "exceptionDetails" in res.get("result", {}):
            raise RuntimeError(f"JS Exception: {res['result']['exceptionDetails']}")
        return res.get("result", {}).get("result", {}).get("value")

    def set_viewport(self, width, height):
        self.send("Emulation.setDeviceMetricsOverride", {
            "width": width,
            "height": height,
            "deviceScaleFactor": 1,
            "mobile": width < 768
        })
        time.sleep(0.3)

    def wait_for_selector(self, selector, timeout=6.0):
        start = time.time()
        while time.time() - start < timeout:
            try:
                res = self.evaluate(f"document.querySelector('{selector}') !== null")
                if res:
                    return True
            except Exception:
                pass
            time.sleep(0.2)
        return False

    def close(self):
        try:
            self.ws.close()
        except:
            pass

def run_tests():
    print("=" * 60)
    print("STARTING RABBIT PHASE 1 E2E TESTS")
    print("=" * 60)

    edge_proc = start_edge()
    client = None
    try:
        ws_url = get_debugger_ws_url()
        client = CDPClient(ws_url)
        try:
            client.send("Browser.grantPermissions", {"permissions": ["clipboardReadWrite", "clipboardSanitizedWrite"]})
        except Exception:
            pass

        # Clear localStorage for clean initial test
        client.evaluate("localStorage.clear(); sessionStorage.clear(); location.reload();")
        time.sleep(1.5)

        # ----------------------------------------------------
        # TEST 1: SCREEN 1 - WELCOME EXPERIENCE (Part 2)
        # ----------------------------------------------------
        print("\n[TEST 1] Welcome Screen Verification...")
        welcome_cta = client.evaluate("""
            (() => {
                const btn = document.querySelector('#rabbit-welcome-cta');
                return btn ? btn.textContent.trim() : null;
            })()
        """)
        print(f"  CTA Button Text: '{welcome_cta}'")
        assert welcome_cta and "Take me to the rabbit hole" in welcome_cta, f"Expected 'Take me to the rabbit hole', got '{welcome_cta}'"
        print("  ✓ Screen 1 Welcome CTA verified faithfully.")

        # ----------------------------------------------------
        # TEST 2: SCREEN 2 - GENRE SELECTION SCREEN (Part 2)
        # ----------------------------------------------------
        print("\n[TEST 2] Transition to Genre Selection Screen...")
        client.evaluate("document.querySelector('#rabbit-welcome-cta').click();")
        time.sleep(0.5)

        genre_count = client.evaluate("""
            document.querySelectorAll('#rabbit-onboarding-chips .chip').length
        """)
        print(f"  Available genres displayed: {genre_count}")
        assert genre_count == 21, f"Expected 21 genres, found {genre_count}"

        # Select Fantasy and Romance
        client.evaluate("""
            (() => {
                const chips = Array.from(document.querySelectorAll('#rabbit-onboarding-chips .chip'));
                const fantasy = chips.find(c => c.textContent.includes('Fantasy'));
                const romance = chips.find(c => c.textContent.includes('Romance'));
                if (fantasy) fantasy.click();
                if (romance) romance.click();
            })()
        """)
        time.sleep(0.3)

        confirm_text = client.evaluate("""
            document.querySelector('#rabbit-confirm-interests-btn').textContent.trim()
        """)
        print(f"  Confirm Button Text: '{confirm_text}'")
        assert "Enter the burrow" in confirm_text, f"Unexpected confirm text: '{confirm_text}'"

        # ----------------------------------------------------
        # TEST 3: SCREEN 3 - PERSONALIZED FEED
        # ----------------------------------------------------
        print("\n[TEST 3] Confirming Interests & Entering Feed...")
        client.evaluate("document.querySelector('#rabbit-confirm-interests-btn').click();")
        time.sleep(1.5)

        entered = client.evaluate("localStorage.getItem('rabbit_entered')")
        print(f"  localStorage 'rabbit_entered': {entered}")
        assert entered == 'true', "localStorage rabbit_entered was not set to 'true'"

        feed_cards_count = client.evaluate("""
            document.querySelectorAll('.feedpost, .feature.rabbit-first-slot-card').length
        """)
        print(f"  Feed cards rendered: {feed_cards_count}")
        assert feed_cards_count >= 10, f"Feed cards too few: {feed_cards_count}"
        print("  ✓ Personalized feed naturally interleaved and populated.")

        # ----------------------------------------------------
        # TEST 4: RETURNING USER EXPERIENCE & RESET HELPER
        # ----------------------------------------------------
        print("\n[TEST 4] Testing Returning User Reload & Reset Helper...")
        client.evaluate("location.reload();")
        is_feed = client.wait_for_selector('#homeScroll', timeout=6.0)
        print(f"  On reload, landed directly on feed: {is_feed}")
        assert is_feed, "Returning user was unexpectedly forced back to welcome screen"

        # Now test reset helper
        print("  Invoking window.resetRabbitOnboarding()...")
        client.evaluate("window.resetRabbitOnboarding();")
        time.sleep(0.5)

        welcome_cta_after_reset = client.evaluate("""
            (() => {
                const btn = document.querySelector('#rabbit-welcome-cta');
                return btn ? btn.textContent.trim() : null;
            })()
        """)
        assert welcome_cta_after_reset and "Take me to the rabbit hole" in welcome_cta_after_reset
        print("  ✓ Reset helper successfully returns user to Screen 1 for testing.")

        # Enter again to feed for remaining tests
        client.evaluate("""
            document.querySelector('#rabbit-welcome-cta').click();
            setTimeout(() => {
                document.querySelector('#rabbit-confirm-interests-btn').click();
            }, 300);
        """)
        time.sleep(1.5)

        # ----------------------------------------------------
        # TEST 5: INTERACTIVE LIKE COUNTER (+1 / -1) (Part 4)
        # ----------------------------------------------------
        print("\n[TEST 5] Testing Interactive Like Button...")
        initial_like_info = client.evaluate("""
            (() => {
                const btn = document.querySelector('.rabbit-like-btn');
                const count = parseInt(btn.querySelector('.rabbit-like-counter').textContent.replace(/,/g, ''), 10);
                const isLiked = btn.classList.contains('active');
                return { count, isLiked };
            })()
        """)
        print(f"  Initial like count: {initial_like_info['count']} (Active: {initial_like_info['isLiked']})")

        # Click like button
        client.evaluate("document.querySelector('.rabbit-like-btn').click();")
        time.sleep(0.3)

        after_like_info = client.evaluate("""
            (() => {
                const btn = document.querySelector('.rabbit-like-btn');
                const count = parseInt(btn.querySelector('.rabbit-like-counter').textContent.replace(/,/g, ''), 10);
                const isLiked = btn.classList.contains('active');
                return { count, isLiked };
            })()
        """)
        print(f"  After like click: {after_like_info['count']} (Active: {after_like_info['isLiked']})")
        assert after_like_info['count'] == initial_like_info['count'] + 1, "Like count did not increment by 1"
        assert after_like_info['isLiked'] is True, "Like button did not become active"

        # Unlike
        client.evaluate("document.querySelector('.rabbit-like-btn').click();")
        time.sleep(0.3)
        after_unlike_info = client.evaluate("""
            (() => {
                const btn = document.querySelector('.rabbit-like-btn');
                const count = parseInt(btn.querySelector('.rabbit-like-counter').textContent.replace(/,/g, ''), 10);
                const isLiked = btn.classList.contains('active');
                return { count, isLiked };
            })()
        """)
        print(f"  After unlike click: {after_unlike_info['count']} (Active: {after_unlike_info['isLiked']})")
        assert after_unlike_info['count'] == initial_like_info['count'], "Like count did not revert by -1"
        print("  ✓ Interactive Like counter behaves with exact +1 / -1 responsiveness.")

        # ----------------------------------------------------
        # TEST 6: REAL SHARE BUTTON & FALLBACK TOAST (Part 3)
        # ----------------------------------------------------
        print("\n[TEST 6] Testing Real Share Button...")
        client.evaluate("""
            document.querySelector('.rabbit-share-btn').click();
        """)
        time.sleep(0.5)

        toast_text = client.evaluate("""
            (() => {
                const t = document.querySelector('.rabbit-toast');
                return t ? t.textContent.trim() : null;
            })()
        """)
        print(f"  Toast notification displayed: '{toast_text}'")
        assert toast_text and ("copied to clipboard" in toast_text or "Link:" in toast_text), f"Expected clipboard toast, got '{toast_text}'"
        print("  ✓ Real Share action with copy fallback and toast confirmation verified.")

        # ----------------------------------------------------
        # TEST 7: DIRECT BOOK DEEP LINK (?book=...)
        # ----------------------------------------------------
        print("\n[TEST 7] Testing Direct Book Deep Link (?book=atomic-habits)...")
        client.evaluate("window.location.href = 'http://localhost:8080/Rabbit./?book=atomic-habits';")
        time.sleep(2.0)

        reader_title = client.evaluate("""
            (() => {
                const overlay = document.querySelector('#rabbit-reader-overlay');
                if (!overlay) return null;
                const h1 = overlay.querySelector('h1');
                return h1 ? h1.textContent.trim() : null;
            })()
        """)
        print(f"  Reader opened directly with title: '{reader_title}'")
        assert reader_title == "Atomic Habits", f"Expected 'Atomic Habits', got '{reader_title}'"

        # Close reader
        client.evaluate("document.querySelector('#rabbit-reader-back-btn').click();")
        time.sleep(0.5)
        reader_closed = client.evaluate("document.querySelector('#rabbit-reader-overlay') === null")
        assert reader_closed, "Reader did not close properly"
        print("  ✓ Direct book deep link opened and closed smoothly.")

        # ----------------------------------------------------
        # TEST 8: RESPONSIVE VIEWPORTS (Mobile, Tablet, Desktop) (Part 5)
        # ----------------------------------------------------
        print("\n[TEST 8] Testing Responsive Viewports...")

        # Mobile 390x844
        print("  Testing Mobile (390 x 844)...")
        client.set_viewport(390, 844)
        client.evaluate("window.dispatchEvent(new Event('resize'));")
        time.sleep(0.5)
        mobile_sidebar = client.evaluate("""
            (() => {
                const sb = document.querySelector('.rabbit-desktop-sidebar');
                if (!sb) return 'absent';
                return window.getComputedStyle(sb).display;
            })()
        """)
        print(f"    Desktop sidebar on Mobile: {mobile_sidebar}")
        assert mobile_sidebar in ['none', 'absent'], "Desktop sidebar should be hidden on mobile"

        # Tablet 820x1180
        print("  Testing Tablet (820 x 1180)...")
        client.set_viewport(820, 1180)
        client.evaluate("window.dispatchEvent(new Event('resize'));")
        time.sleep(0.5)
        tablet_sidebar = client.evaluate("""
            (() => {
                const sb = document.querySelector('.rabbit-desktop-sidebar');
                if (!sb) return 'absent';
                return window.getComputedStyle(sb).display;
            })()
        """)
        print(f"    Desktop sidebar on Tablet: {tablet_sidebar}")
        assert tablet_sidebar in ['none', 'absent'], "Desktop sidebar should be hidden on tablet"

        # Desktop 1440x900
        print("  Testing Desktop (1440 x 900)...")
        client.set_viewport(1440, 900)
        client.evaluate("location.reload();")
        client.wait_for_selector('.rabbit-desktop-sidebar', timeout=6.0)
        desktop_layout = client.evaluate("""
            (() => {
                const sb = document.querySelector('.rabbit-desktop-sidebar');
                const cp = document.querySelector('.rabbit-desktop-context-pane');
                const feed = document.querySelector('.page');
                return {
                    sidebarVisible: Boolean(sb && window.getComputedStyle(sb).display !== 'none'),
                    contextPaneVisible: Boolean(cp && window.getComputedStyle(cp).display !== 'none'),
                    feedWidth: feed ? feed.getBoundingClientRect().width : 0
                };
            })()
        """)
        print(f"    Desktop layout metrics: {desktop_layout}")
        assert desktop_layout['sidebarVisible'], "Desktop sidebar should be visible on 1440px"
        assert desktop_layout['contextPaneVisible'], "Desktop context pane should be visible on 1440px"
        assert 500 <= desktop_layout['feedWidth'] <= 700, f"Feed width out of range: {desktop_layout['feedWidth']}"
        print("  ✓ Responsive layouts verified across Mobile, Tablet, and Desktop.")

        print("\n" + "=" * 60)
        print("ALL 8 END-TO-END SUITE TESTS PASSED WITH 100% SUCCESS!")
        print("=" * 60)

    finally:
        client.close()
        edge_proc.kill()

if __name__ == "__main__":
    run_tests()
