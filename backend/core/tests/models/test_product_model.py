from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase

from core.models import Product, Status

User = get_user_model()


class ProductModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test",
            password="test",
        )

        self.product = Product.objects.create(
            title="Product #1",
            description="Product #1 description",
            date=date.today(),
        )

    def test_str_representation(self):
        self.assertEqual(
            str(self.product),
            f"({self.product.id}) - {self.product.title}",
        )

    def test_default_status_is_active(self):
        self.assertEqual(self.product.status, Status.ACTIVE)

    def test_can_favorite_product(self):
        self.product.favorites.add(self.user)

        self.assertTrue(self.product.favorites.filter(id=self.user.id).exists())

    def test_can_unfavorite_product(self):
        self.product.favorites.add(self.user)
        self.product.favorites.remove(self.user)

        self.assertFalse(self.product.favorites.filter(id=self.user.id).exists())
