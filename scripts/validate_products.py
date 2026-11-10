import json
import sys
from pathlib import Path

p = Path('data/products.json')
data = json.loads(p.read_text(encoding='utf-8'))
errors = []
required = {'id', 'name', 'store', 'category_id', 'category_name', 'description', 'price', 'currency', 'affiliate_url', 'last_checked', 'demo'}
ids = set()
cats = {c['id'] for c in data.get('categories', [])}

for i, item in enumerate(data.get('products', []), 1):
    missing = required - set(item)
    if missing:
        errors.append(f'product {i}: missing {sorted(missing)}')
    if item.get('id') in ids:
        errors.append(f'product {i}: duplicate id')
    ids.add(item.get('id'))
    if item.get('category_id') not in cats:
        errors.append(f"product {i}: unknown category {item.get('category_id')}")
    if item.get('price') is not None and (not isinstance(item['price'], (int, float)) or item['price'] < 0):
        errors.append(f'product {i}: invalid price')
    if not item.get('demo') and (item.get('price') is None or item.get('affiliate_url') in (None, '#')):
        errors.append(f"product {i}: published products need verified price and affiliate_url")

if data.get('data_status') != 'DEMO_ONLY':
    for item in data.get('products', []):
        if item.get('demo'):
            errors.append(f"{item.get('id')}: demo item cannot be mixed into live data without review")

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f"Validated {len(data.get('products', []))} products and {len(data.get('categories', []))} categories.")
