#!/usr/bin/env python3
"""Check a public GitHub Pages Jekyll site and its article links. No dependencies."""
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen
import sys


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.article_hrefs = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "story-card" in attrs.get("class", "").split():
            href = attrs.get("href")
            if href and href not in self.article_hrefs:
                self.article_hrefs.append(href)


def get_page(url):
    req = Request(url, headers={"User-Agent": "ArticleReaderSiteCheck/1.0"})
    with urlopen(req, timeout=20) as response:
        if response.status != 200:
            raise RuntimeError(f"HTTP {response.status}: {url}")
        return response.read().decode("utf-8", errors="replace")


def verify(url):
    if not url.endswith("/"):
        url += "/"
    if urlparse(url).scheme not in ("http", "https"):
        raise ValueError("Enter the full URL starting with https://")
    homepage = get_page(url)
    if 'class="story-card"' not in homepage:
        raise RuntimeError("Homepage did not render article cards (check GitHub Pages/Jekyll)")
    if "{%" in homepage or "{{" in homepage:
        raise RuntimeError("Unrendered Jekyll markup found (check Pages publishing settings)")
    slots = [f"Advertisement placement {i:02d}" for i in range(1, 9)]
    missing = [s for s in slots if s not in homepage]
    if missing:
        print("WARNING: Not all eight labeled ad slots are visible (they may be hidden intentionally).")
    parser = PageParser()
    parser.feed(homepage)
    links = parser.article_hrefs
    if not links:
        raise RuntimeError("No article links found on homepage")
    failures = []
    for href in links:
        article_url = urljoin(url, href)
        try:
            content = get_page(article_url)
            if 'class="article-body"' not in content or "<h1" not in content:
                raise RuntimeError("Missing article heading/body")
            print(f"PASS article: {article_url}")
        except (HTTPError, URLError, RuntimeError) as exc:
            failures.append(f"{article_url} ({exc})")
    print(f"PASS homepage: {url}")
    print(f"Ad positions found: {8 - len(missing)}/8")
    print(f"Readable article pages: {len(links) - len(failures)}/{len(links)}")
    if failures:
        print("FAILURES:\n" + "\n".join(failures), file=sys.stderr)
        raise SystemExit(1)
    print("SUCCESS: Public homepage and all linked articles are readable.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python scripts/verify_live.py https://USERNAME.github.io/article-reader/")
    try:
        verify(sys.argv[1])
    except (ValueError, HTTPError, URLError, RuntimeError) as exc:
        sys.exit(f"Site check failed: {exc}")
