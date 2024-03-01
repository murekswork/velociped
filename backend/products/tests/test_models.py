from django.contrib.auth import get_user_model
from django.test import TestCase
from products.models import Product


class ProductModelTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username='testproduct', email='testproduct@email.com')
        self.user.set_password('0xABAD1DEA')
        self.product1 = Product.objects.create(user=self.user, title='Test Product 1',
                                               content='Test Product Content', price=100)
        self.product2 = Product.objects.create(user=self.user, title='Test Product 2',
                                               content='Test Product Content', price=500)

    def test_create_product(self):
        self.assertEqual(self.product1.title, 'Test Product 1')
        self.assertEqual(self.product1.content, 'Test Product Content')
        self.assertEqual(self.product1.price, 100)
        self.assertEqual(self.product1.user, self.user)
        self.assertEqual(self.product1.public, True)
        self.assertEqual(self.product2.title, 'Test Product 2')
        self.assertEqual(self.product2.content, 'Test Product Content')
        self.assertEqual(self.product2.price, 500)
        self.assertEqual(self.product2.user, self.user)

    def test_product_str(self):
        self.assertEqual(self.product1.__str__(), 'Test Product 1 for 100 from testproduct')

    def test_product_search_with_one_existing_product(self):
        products = Product.objects.search('Product 1')
        self.assertEqual(products.count(), 1)
        self.assertEqual(products.first(), self.product1)

    def test_product_search_with_two_existing_products(self):
        products = Product.objects.search('Product')
        self.assertEqual(products.count(), 2)
        self.assertEqual(products.first(), self.product1)
        self.assertEqual(products.last(), self.product2)

    def test_product_search_with_non_existing_product(self):
        products = Product.objects.search('Product 3')
        self.assertEqual(products.count(), 0)
