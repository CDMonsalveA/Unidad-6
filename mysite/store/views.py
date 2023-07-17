"""Set Up Views from the api app"""

from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
    ProductSerializer,
    CategorySerializer,
    BrandSerializer,
)
from .models import Product, Category, Brand


@api_view(["GET"])
def apioverview(request):
    """apiOverview"""
    api_urls = {
        "List": "/product-list/",
        "Detail View": "/product-detail/<str:pk>/",
        "Create": "/product-create/",
        "Update": "/product-update/<str:pk>/",
        "Delete": "/product-delete/<str:pk>/",
    }
    return Response(api_urls)

@api_view(["GET"])
def product_list(request):
    """List all products"""
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def product_detail(request, pk):
    """Retrieve a product"""
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)

@api_view(["POST"])
def product_create(request):
    """Create a product"""
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
def product_update(request, pk):
    """Update a product"""
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

