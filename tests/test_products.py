import json
import unittest
from pathlib import Path


class ProductSiteTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(Path('data/products.json').read_text(encoding='utf-8'))

    def test_demo_data_is_explicit(self):
        self.assertEqual(self.data['data_status'], 'DEMO_ONLY')
        self.assertTrue(all(item['demo'] is True for item in self.data['products']))

    def test_products_reference_known_categories(self):
        categories = {c['id'] for c in self.data['categories']}
        self.assertTrue(all(item['category_id'] in categories for item in self.data['products']))

    def test_required_pages_exist(self):
        for path in ['index.html', 'about.html', 'privacy.html', '404.html', 'robots.txt', 'sitemap.xml']:
            self.assertTrue(Path(path).exists(), path)


if __name__ == '__main__':
    unittest.main()
