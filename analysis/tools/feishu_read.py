# -*- coding: utf-8 -*-
"""
Feishu document reader.
Usage:
    python analysis/tools/feishu_read.py <url>
    python analysis/tools/feishu_read.py <url> --out output.txt

Requires feishu_auth.json (run feishu_login.py first).
"""

import sys, argparse
from pathlib import Path
from playwright.sync_api import sync_playwright

AUTH_FILE = Path(__file__).parent / "feishu_auth.json"


def fetch_feishu(url: str) -> str:
    if not AUTH_FILE.exists():
        raise FileNotFoundError("feishu_auth.json not found. Please run feishu_login.py first.")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(
            storage_state=str(AUTH_FILE),
            viewport={"width": 1280, "height": 900},
        )
        page = ctx.new_page()
        page.goto(url, timeout=40000, wait_until="domcontentloaded")

        # Wait for document body to appear
        try:
            page.wait_for_selector(
                ".wiki-content, .docx-content, .page-block-children, [data-block-type]",
                timeout=15000,
            )
        except Exception:
            pass

        # Feishu uses .bear-web-x-container as the real scroll container.
        # Scroll it in small increments to force virtual-scroll to render all blocks.
        scroll_js = """() => {
            const el = document.querySelector('.bear-web-x-container');
            if (!el) return [0, 0];
            el.scrollTop += 300;
            return [el.scrollTop, el.scrollHeight - el.clientHeight];
        }"""
        for _ in range(200):
            result = page.evaluate(scroll_js)
            page.wait_for_timeout(200)
            if result[0] >= result[1]:
                break

        page.wait_for_timeout(1500)

        # Single harvest after full scroll — all blocks now in DOM
        content = page.evaluate("""() => {
            const lines = document.querySelectorAll('.ace-line');
            if (lines.length > 10)
                return Array.from(lines).map(el => el.innerText).join('\\n');
            const zones = document.querySelectorAll('.zone-container');
            if (zones.length > 5)
                return Array.from(zones).map(el => el.innerText).join('\\n');
            let best = '', bestLen = 0;
            document.querySelectorAll('div').forEach(el => {
                const t = el.innerText.trim();
                if (t.length > bestLen) { best = t; bestLen = t.length; }
            });
            return best || document.body.innerText;
        }""")

        browser.close()
        return content.strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Feishu document URL")
    parser.add_argument("--out", "-o", help="Output file path (default: print to stdout)")
    args = parser.parse_args()

    try:
        text = fetch_feishu(args.url)
    except FileNotFoundError as e:
        print("Error:", e)
        sys.exit(1)

    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print("Saved to:", args.out)
    else:
        sys.stdout.buffer.write(text.encode("utf-8"))
        sys.stdout.buffer.write(b"\n")


if __name__ == "__main__":
    main()
