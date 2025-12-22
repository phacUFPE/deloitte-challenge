from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.filters import ProductFilter
from core.models import Product
from core.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
    ]
    search_fields = [
        "title",
        "description",
    ]

    def get_queryset(self):
        return Product.objects.all().prefetch_related("favorites")

    @action(
        detail=True,
        methods=["post"],
        permission_classes=[IsAuthenticated],
    )
    def toggle_favorite(self, request, pk=None):
        product = self.get_object()
        user = request.user

        if product.favorites.filter(id=user.id).exists():
            product.favorites.remove(user)
            favorited = False
        else:
            product.favorites.add(user)
            favorited = True

        return Response({"favorited": favorited})
