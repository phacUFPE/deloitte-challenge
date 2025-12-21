from django.conf import settings
from django.db import models


class Status(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    INACTIVE = "INACTIVE", "Inactive"
    BLOCKED = "BLOCKED", "Blocked"


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField()
    date = models.DateField()
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.ACTIVE
    )

    favorites = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="favorite_products", blank=True
    )

    def __str__(self) -> str:
        return f"({self.id}) - {self.title}"
