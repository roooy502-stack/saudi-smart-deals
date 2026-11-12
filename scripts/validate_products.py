import json
import sys
from pathlib import Path

p = Path('data/products.json')
data = json.loads(p.read_text(encoding='utf-8'))
errors = []
required = {'id', 'name', 'store', 'category_id', 'category_name', 'description', 'price', 'base_price_usd', 'currency', 'affiliate_url', 'source_url', 'image_url', 'available_countries', 'published', 'last_checked', 'demo'}
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
        errors.append(f'product {i}: invalid retail price')
    if item.get('base_price_usd') is not None and (not isinstance(item['base_price_usd'], (int, float)) or item['base_price_usd'] < 0):
        errors.append(f'product {i}: invalid base USD price')
    if not item.get('source_url') or not item.get('image_url') or not item.get('last_checked'):
        errors.append(f"product {i}: sourced products need source_url, image_url and last_checked")
    if item.get('published') and (item.get('price') is None or item.get('affiliate_url') in (None, '#')):
        errors.append(f"product {i}: published products need verified retail price and action URL")

if not data.get('whatsapp_number', '').isdigit():
    errors.append('whatsapp_number must contain digits only in international format')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f"Validated {len(data.get('products', []))} COD Partner products and {len(data.get('categories', []))} categories.")
