# -*- coding: utf-8 -*-
"""
Feishu one-time login tool.
Usage: python analysis/tools/feishu_login.py

Opens a browser window -> SSO auto-login (company intranet) -> saves session to feishu_auth.json.
After this, feishu_read.py can silently read any Feishu document.
"""

import json, os, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

AUTH_FILE = Path(__file__).parent / "feishu_auth.json"


def main():
    print("Opening browser, visiting Feishu...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        ctx = browser.new_context()
        page = ctx.new_page()
        page.goto("https://nio.feishu.cn", timeout=30000)

        page.wait_for_timeout(4000)

        current_url = page.url
        if "passport" in current_url or "login" in current_url:
            print("Login page detected. Waiting for you to complete login in the browser (up to 120s)...")
            page.wait_for_url(lambda url: "passport" not in url and "login" not in url, timeout=120000)
            print("Login complete. Current page:", page.url)
        else:
            print("SSO auto-login success. Current page:", current_url)

        storage = ctx.storage_state()
        AUTH_FILE.write_text(json.dumps(storage, ensure_ascii=False, indent=2), encoding="utf-8")
        print("Session saved to:", AUTH_FILE)
        browser.close()


if __name__ == "__main__":
    main()
