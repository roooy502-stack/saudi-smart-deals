from pathlib import Path
from html.parser import HTMLParser
import sys

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.title = ''
        self.desc = False
        self.lang = None

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        attrs = dict(attrs)
        if tag == 'html':
            self.lang = attrs.get('lang')
        if tag == 'meta' and attrs.get('name') == 'description' and attrs.get('content'):
            self.desc = True

    def handle_data(self, data):
        if self.tags and self.tags[-1] == 'title':
            self.title += data

    def handle_endtag(self, tag):
        if self.tags and self.tags[-1] == tag:
            self.tags.pop()

errors = []
for path in Path('.').glob('*.html'):
    text = path.read_text(encoding='utf-8')
    parser = PageParser()
    parser.feed(text)
    if parser.lang != 'ar':
        errors.append(f'{path}: expected lang=ar')
    if 'dir="rtl"' not in text[:300]:
        errors.append(f'{path}: expected dir=rtl')
    if not parser.title.strip():
        errors.append(f'{path}: missing title')
    if not parser.desc:
        errors.append(f'{path}: missing meta description')
if not Path('robots.txt').exists():
    errors.append('robots.txt missing')
if not Path('sitemap.xml').exists():
    errors.append('sitemap.xml missing')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'SEO audit passed for {len(list(Path(".").glob("*.html")))} HTML pages.')
