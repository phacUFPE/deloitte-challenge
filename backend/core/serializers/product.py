from rest_framework import serializers

from core.models import Product


class ProductSerializer(serializers.ModelSerializer):
    favorites = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Product
        fields = "__all__"
