import json
import unittest
from pathlib import Path


class ProductSiteTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(Path('data/products.json').read_text(encoding='utf-8'))

    def test_codpartner_source_is_explicit(self):
        self.assertEqual(self.data['data_status'], 'CODPARTNER_CATALOG_PENDING')
        self.assertEqual(self.data['source_platform'], 'COD Partner')
        self.assertTrue(self.data['whatsapp_number'].isdigit())

    def test_products_reference_known_categories_and_saudi(self):
        categories = {c['id'] for c in self.data['categories']}
        self.assertTrue(all(item['category_id'] in categories for item in self.data['products']))
        self.assertTrue(all('SA' in item['available_countries'] for item in self.data['products']))
        self.assertTrue(all(item['source_url'].startswith('https://') for item in self.data['products']))

    def test_products_are_pending_until_final_price_and_order_flow_are_confirmed(self):
        self.assertTrue(all(item['published'] is False for item in self.data['products']))
        self.assertTrue(all(item['price'] is None for item in self.data['products']))

    def test_required_pages_exist(self):
        for path in ['index.html', 'about.html', 'privacy.html', '404.html', 'robots.txt', 'sitemap.xml']:
            self.assertTrue(Path(path).exists(), path)


if __name__ == '__main__':
    unittest.main()
