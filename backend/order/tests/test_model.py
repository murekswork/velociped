from django.contrib.auth import get_user_model
from django.test import TestCase
from order.models import Order
from order.services.order_service import OrderServiceFabric
from products.models import Product
from wallet.models import Wallet


class OrderModelTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username='test', email='test@test.com')
        self.user.set_password('0xABAD1DEA')
        self.user_wallet = Wallet.objects.create(user=self.user, balance=100000)
        self.order_product = Product.objects.create(user=self.user, title='product', price=100)
        self.order = Order.objects.create(user=self.user, product=self.order_product, count=5)

    def test_product_field(self):
        self.assertEqual(self.order.product, self.order_product)

    def test_user_field(self):
        self.assertEqual(self.order.user, self.user)

    def test_count_field(self):
        self.assertEqual(self.order.count, 5)

    def test_amount_field(self):
        self.assertEqual(int(self.order.amount), 0)

    def test_total_amount_property(self):
        self.assertEqual(float(self.order.total_amount), float(self.order_product.price * self.order.count))

    def test_payment_status_field(self):
        self.assertEqual(self.order.payment_status, False)

    def test_payment_status_field_when_payed(self):
        self.order_product.quantity = 50
        self.order_product.save()
        service = OrderServiceFabric.get_order_service(self.order)
        service.pay_order()
        self.assertEqual(self.order.payment_status, True)
