"""Add two links to the shared Jekyll footer without overwriting customizations."""
from pathlib import Path
import re
import sys

layout_path = Path(__file__).resolve().parents[1] / "_layouts" / "default.html"
if not layout_path.is_file():
    sys.exit("ERROR: Missing _layouts/default.html in this project.")

with layout_path.open("r", encoding="utf-8", newline="") as f:
    original = f.read()

pattern = re.compile(r'''(<nav\b[^>]*\baria-label=["']Footer navigation["'][^>]*>)(.*?)(</nav>)''', re.I | re.S)
match = pattern.search(original)
if not match:
    sys.exit("ERROR: Footer navigation not found. No files changed.")

inner = match.group(2)
links = [
    ("/latest.html", "Latest Article"),
    ("/reading-list.html", "Reading List"),
]
for url, label in links:
    if url not in inner:
        inner += '<a href="{{ \'%s\' | relative_url }}">%s</a>' % (url, label)

updated = original[:match.start()] + match.group(1) + inner + match.group(3) + original[match.end():]
if updated != original:
    with layout_path.open("w", encoding="utf-8", newline="") as f:
        f.write(updated)
    print("Added 2 footer links for all pages.")
else:
    print("Both footer links are already present.")
