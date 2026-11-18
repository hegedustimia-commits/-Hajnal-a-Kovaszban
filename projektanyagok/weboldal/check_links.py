from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

root = Path(__file__).resolve().parent.parent.parent / 'public'

class Refs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []

    def handle_starttag(self, tag, attrs):
        self.refs += [value for key, value in attrs if key in ('href', 'src') and value]

missing = []
for file in root.glob('*.html'):
    parser = Refs()
    parser.feed(file.read_text(encoding='utf-8'))
    for ref in parser.refs:
        if ref.startswith(('http:', 'https:', 'mailto:', '#')):
            continue
        path = root / unquote(urlsplit(ref).path)
        if not path.exists():
            missing.append((file.name, ref))

print(f'HTML pages: {len(list(root.glob("*.html")))}; missing local targets: {missing}')
if missing:
    raise SystemExit(1)
