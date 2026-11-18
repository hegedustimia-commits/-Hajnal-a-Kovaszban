"""Check the generated site's basic SEO metadata and local references."""

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree
import json

SITE = Path(__file__).resolve().parents[2] / "public"


class PageAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.in_schema = False
        self.schema_text = ""
        self.meta = {}
        self.canonical = None
        self.headings = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "script" and attrs.get("type") == "application/ld+json":
            self.in_schema = True
        elif tag == "meta":
            self.meta[attrs.get("name") or attrs.get("property")] = attrs.get("content")
        elif tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        elif tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.headings.append(int(tag[1]))
        elif tag == "img":
            self.images.append(attrs)

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "script":
            self.in_schema = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        if self.in_schema:
            self.schema_text += data


errors = []
titles, descriptions = set(), set()
indexable_urls = set()
for path in sorted(SITE.glob("*.html")):
    page = PageAudit()
    page.feed(path.read_text(encoding="utf-8"))
    label = path.name
    description = page.meta.get("description")
    if not page.title or page.title in titles:
        errors.append(f"{label}: missing or repeated title")
    if not description or description in descriptions:
        errors.append(f"{label}: missing or repeated description")
    titles.add(page.title)
    descriptions.add(description)
    if page.headings.count(1) != 1 or page.headings[0] != 1:
        errors.append(f"{label}: expected one leading h1")
    if any(b > a + 1 for a, b in zip(page.headings, page.headings[1:])):
        errors.append(f"{label}: skipped heading level")
    if any(not image.get("alt") for image in page.images):
        errors.append(f"{label}: image without descriptive alt")
    if not page.canonical or urlparse(page.canonical).scheme != "https":
        errors.append(f"{label}: invalid canonical URL")
    for key in ("og:type", "og:locale", "og:title", "og:description", "og:url", "og:image", "og:image:alt"):
        if not page.meta.get(key):
            errors.append(f"{label}: missing {key}")
    if page.meta.get("og:url") != page.canonical:
        errors.append(f"{label}: Open Graph URL differs from canonical")
    image_url = page.meta.get("og:image", "")
    image_name = image_url.rsplit("/", 1)[-1]
    if not (SITE / "assets" / image_name).is_file():
        errors.append(f"{label}: Open Graph image is missing")
    if page.schema_text:
        business = json.loads(page.schema_text)
        if business.get("@type") != "Bakery" or not business.get("address") or not business.get("openingHoursSpecification"):
            errors.append(f"{label}: incomplete Bakery structured data")
    elif path.stem in {"index", "kapcsolat"}:
        errors.append(f"{label}: missing Bakery structured data")
    if page.meta.get("robots") != "noindex, follow":
        indexable_urls.add(page.canonical)

root = ElementTree.parse(SITE / "sitemap.xml").getroot()
sitemap_urls = {node.text for node in root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc")}
if sitemap_urls != indexable_urls:
    errors.append("sitemap.xml differs from indexable page URLs")
robots = (SITE / "robots.txt").read_text(encoding="utf-8")
domain = urlparse(next(iter(indexable_urls))).netloc
if f"Sitemap: https://{domain}/sitemap.xml" not in robots:
    errors.append("robots.txt has no sitemap URL")

print(f"Checked {len(titles)} HTML pages and {len(sitemap_urls)} sitemap URLs")
if errors:
    raise SystemExit("\n".join(errors))
