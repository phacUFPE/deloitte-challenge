from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Product
from core.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

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
