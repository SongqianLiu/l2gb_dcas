# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
from pathlib import Path
from playwright.sync_api import sync_playwright

AUTH_FILE = Path(__file__).parent / "feishu_auth.json"

PAGES = [
    ("系统禁用",       "https://nio.feishu.cn/wiki/BfxvwS8x3i7De7kDkj1ci8Qxnce"),
    ("Lane_Change",   "https://nio.feishu.cn/wiki/M8T8wEx3xiODOQk8vSDcO3HPnnh"),
    ("可控性需求",     "https://nio.feishu.cn/wiki/AyeYwuJcQiGlzbkJGYeceJfpnhc"),
    ("避免驾驶员误用", "https://nio.feishu.cn/wiki/A40ywdzvfiLzwMkUhGoczA1vnEe"),
    ("Speed_Limit",   "https://nio.feishu.cn/wiki/McKEw9XM2iq8smktN0xcwHwdnFb"),
    ("ODC_failsafe",  "https://nio.feishu.cn/wiki/BhzdwbHe0i7rUZkmIhEc6v5mnxg"),
    ("ODC_速度范围",   "https://nio.feishu.cn/wiki/Oe6KwScxli6YBbk8YfuclpW8nDf"),
    ("ODC_场景",      "https://nio.feishu.cn/wiki/YbXJw35npip8KRkn3fpcZ3DCn0f"),
    ("TLD",          "https://nio.feishu.cn/wiki/KoegwPFhKibESSkBsFOcCVdPnGg"),
    ("HMI_General",  "https://nio.feishu.cn/wiki/HPCNwYXqFi6GOGkJGqtcJConnwr"),
    ("产品说明",      "https://nio.feishu.cn/wiki/MyZnwTFSni0KlIkFYU6cllkpnad"),
]

EXTRACT_JS = "() => { const lines = document.querySelectorAll('.ace-line'); if (lines.length > 10) return Array.from(lines).map(el => el.innerText).join('\\n'); const zones = document.querySelectorAll('.zone-container'); if (zones.length > 5) return Array.from(zones).map(el => el.innerText).join('\\n'); let best = '', bestLen = 0; document.querySelectorAll('div').forEach(el => { const t = el.innerText.trim(); if (t.length > bestLen) { best = t; bestLen = t.length; } }); return best || document.body.innerText; }"

SCROLL_JS = "() => { const el = document.querySelector('.bear-web-x-container'); if (!el) return [0, 0]; el.scrollTop += 300; return [el.scrollTop, el.scrollHeight - el.clientHeight]; }"

OUT_DIR = Path(__file__).parent.parent.parent / "notes"


def read_page(page, url):
    page.goto(url, timeout=40000, wait_until="domcontentloaded")
    try:
        page.wait_for_selector(
            ".wiki-content, .docx-content, .bear-web-x-container, [data-block-type]",
            timeout=15000,
        )
    except Exception:
        pass
    for _ in range(200):
        result = page.evaluate(SCROLL_JS)
        page.wait_for_timeout(150)
        if result[0] >= result[1]:
            break
    page.wait_for_timeout(1000)
    return page.evaluate(EXTRACT_JS).strip()


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        ctx = browser.new_context(
            storage_state=str(AUTH_FILE),
            viewport={"width": 1280, "height": 900},
        )
        pg = ctx.new_page()

        for name, url in PAGES:
            out = OUT_DIR / f"adrs_{name}.txt"
            try:
                content = read_page(pg, url)
                out.write_text(content, encoding="utf-8")
                print(f"OK  {name} -> {out.name} ({len(content)} chars)")
            except Exception as e:
                print(f"ERR {name}: {e}")

        browser.close()


if __name__ == "__main__":
    main()
