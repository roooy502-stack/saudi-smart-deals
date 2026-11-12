import json
import math
import sys
from pathlib import Path


data = json.loads(Path('data/products.json').read_text(encoding='utf-8'))
a = data['pricing_assumptions']
rate = float(a['exchange_rate_usd_sar'])
shipping = float(a['ksa_delivered_shipping_usd']) * rate
cod_rate = float(a['cod_fee_percent']) / 100
margin = float(a['target_net_margin_percent']) / 100
errors = []

for item in data['products']:
    fees = a[f"{item['product_type']}_fees_usd"]
    base_cost = float(item['base_price_usd']) * rate
    service_cost = sum(float(v) for v in fees.values()) * rate
    total_before_cod = base_cost + service_cost + shipping
    minimum = total_before_cod / (1 - cod_rate - margin)
    proposed = float(item['estimated_price_sar'])
    net = proposed * (1 - cod_rate) - total_before_cod
    net_margin = net / proposed
    if proposed + 1e-9 < minimum:
        errors.append(f"{item['id']}: proposed price {proposed:.2f} SAR is below minimum {minimum:.2f} SAR")
    print(f"{item['name']}: proposed={proposed:.2f} SAR, estimated net={net:.2f} SAR, margin={net_margin:.1%}")

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('Pricing audit passed. Estimates exclude advertising spend, returns, taxes, and any tariff changes.')
