from pathlib import Path
import re
import sys

errors = []
for path in Path('.').glob('*.html'):
    text = path.read_text(encoding='utf-8')
    for href in re.findall(r'href=["\\\']([^"\\\'#?]+)', text):
        if href.startswith(('http://', 'https://', 'mailto:')):
            continue
        target = (path.parent / href).resolve()
        if not target.exists():
            errors.append(f'{path}: missing {href}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('Local link check passed.')
