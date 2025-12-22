from datetime import timedelta
from random import choice

from django.core.management.base import BaseCommand
from faker import Faker

from core.models import Product, Status


class Command(BaseCommand):
    help = "Seed database with fake products"

    def add_arguments(self, parser):
        parser.add_argument(
            "--total",
            type=int,
            default=100,
            help="Number of products to create (default: 100)",
        )

    def handle(self, *args, **options):
        total = options["total"]

        fake = Faker("pt_BR")

        statuses = [
            Status.ACTIVE,
            Status.INACTIVE,
            Status.BLOCKED,
        ]

        start_date = fake.date_between(start_date="-1y", end_date="today")

        products = []

        for i in range(total):
            products.append(
                Product(
                    title=fake.catch_phrase()[:100],
                    description=fake.text(max_nb_chars=250),
                    image=f"products/product_{i+1:03}.jpg",
                    date=start_date + timedelta(days=i),
                    status=choice(statuses),
                )
            )

        Product.objects.bulk_create(products)

        self.stdout.write(self.style.SUCCESS(f"{total} products created!"))
