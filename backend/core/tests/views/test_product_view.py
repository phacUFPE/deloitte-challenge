from datetime import date

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from core.models import Product, Status

User = get_user_model()


def generate_products_given_amount(amount: int = 10):
    products = []
    for i in range(0, amount):
        product = Product.objects.create(
            title=f"Product #{i}",
            description=f"Product #{i} description",
            date=date.today(),
        )
        products.append(product)

    return products


class ListProductTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.products_amount = 25
        cls.products = generate_products_given_amount(cls.products_amount)

    def test_list_all(self):
        response = self.client.get("/products/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), self.products_amount)

    def test_search(self):
        Product.objects.create(
            title="Search Product",
            description="Search Product description",
            date=date.today(),
        )
        response = self.client.get("/products/?search=search")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_filter_status(self):
        product1 = self.products[0]
        product2 = self.products[1]

        product1.status = Status.BLOCKED
        product1.save()

        product2.status = Status.BLOCKED
        product2.save()

        response = self.client.get("/products/?status=BLOCKED")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)


class FavoriteProductTest(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.products = generate_products_given_amount()
        cls.user = User.objects.create_user(
            username="test",
            password="test",
        )

    def test_toggle_favorite_true_with_logged_user(self):
        self.client.force_authenticate(self.user)

        product = self.products[0]

        response = self.client.post(f"/products/{product.id}/toggle_favorite/")

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["favorited"])
        self.assertTrue(
            Product.objects.get(pk=product.id)
            .favorites.filter(id=self.user.id)
            .exists()
        )

    def test_toggle_favorite_true_without_logged_user(self):
        response = self.client.post(f"/products/{self.products[0].id}/toggle_favorite/")

        self.assertEqual(response.status_code, 403)

    def test_toggle_favorite_false_with_logged_user(self):
        self.client.force_authenticate(self.user)

        product = self.products[0]

        self.client.post(f"/products/{product.id}/toggle_favorite/")
        responseToggleFalse = self.client.post(
            f"/products/{product.id}/toggle_favorite/"
        )

        self.assertEqual(responseToggleFalse.status_code, 200)
        self.assertFalse(responseToggleFalse.data["favorited"])
        self.assertFalse(
            Product.objects.get(pk=product.id)
            .favorites.filter(id=self.user.id)
            .exists()
        )
