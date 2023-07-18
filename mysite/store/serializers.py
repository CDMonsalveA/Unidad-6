"""store Serializers"""
from rest_framework import serializers
from .models import Product, Category, Brand


# ProductSerializer
#   - id
#   - name
#   - description
#   - price
#   - image
#   - category
#   - brand
#   - stock
class ProductSerializer(serializers.ModelSerializer):
    """Serializer definition for Product."""

    class Meta:
        """Meta definition for ProductSerializer."""

        model = Product
        fields = "__all__"


# CategorySerializer
#   - id
#   - name
class CategorySerializer(serializers.ModelSerializer):
    """Serializer definition for Category."""

    class Meta:
        """Meta definition for CategorySerializer."""

        model = Category
        fields = "__all__"


# BrandSerializer
#   - id
#   - name
class BrandSerializer(serializers.ModelSerializer):
    """Serializer definition for Brand."""

    class Meta:
        """Meta definition for BrandSerializer."""

        model = Brand
        fields = "__all__"

# 
