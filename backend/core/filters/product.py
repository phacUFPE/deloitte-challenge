import django_filters

from core.models import Product


class ProductFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(
        field_name="status",
    )
    date_from = django_filters.DateFilter(
        field_name="date",
        lookup_expr="gte",
    )
    date_to = django_filters.DateFilter(
        field_name="date",
        lookup_expr="lte",
    )

    class Meta:
        model = Product
        fields = [
            "status",
            "date_from",
            "date_to",
        ]
