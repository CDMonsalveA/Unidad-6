"""Set Up Views from the api app"""
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Product, Category, Brand
from .serializers import ProductSerializer, CategorySerializer, BrandSerializer


def all_products(request):
    """A view to show all products, including sorting and search queries"""
    products = Product.objects.all()  # pylint: disable=no-member
    prices = sorted(
        Product.objects.all().values_list("price", flat=True) # pylint: disable=no-member
    )  # pylint: disable=no-member
    categories = Category.objects.all()  # pylint: disable=no-member
    brands = Brand.objects.all()  # pylint: disable=no-member
    context = {
        "products": products,
        "categories": categories,
        "brands": brands,
        "prices": prices,
    }
    return render(request, "products.html", context)


def product_per_category(request, category_name):
    """A view to show products per category"""
    products = Product.objects.filter( # pylint: disable=no-member
        category__name=category_name
    )  # pylint: disable=no-member
    prices = sorted(
        Product.objects.filter(category__name=category_name).values_list( # pylint: disable=no-member
            "price", flat=True
        )
    )  # pylint: disable=no-member
    categories = Category.objects.all()  # pylint: disable=no-member
    brands = Brand.objects.all()  # pylint: disable=no-member
    context = {
        "products": products,
        "categories": categories,
        "brands": brands,
        "prices": prices,
    }
    return render(request, "products.html", context)


def product_per_brand(request, brand_name):
    """A view to show products per brand"""
    products = Product.objects.filter( # pylint: disable=no-member
        brand__name=brand_name
    )  # pylint: disable=no-member
    prices = sorted(
        Product.objects.filter(brand__name=brand_name).values_list("price", flat=True) # pylint: disable=no-member
    )  # pylint: disable=no-member
    categories = Category.objects.all()  # pylint: disable=no-member
    brands = Brand.objects.all()  # pylint: disable=no-member
    context = {
        "products": products,
        "categories": categories,
        "brands": brands,
        "prices": prices,
    }
    return render(request, "products.html", context)


def product_by_price(request, price):
    """A view to show products by price"""
    products = Product.objects.filter(price=price)  # pylint: disable=no-member
    prices = sorted(
        Product.objects.filter(price=price).values_list("price", flat=True) # pylint: disable=no-member
    )  # pylint: disable=no-member
    categories = Category.objects.all() # pylint: disable=no-member
    brands = Brand.objects.all()  # pylint: disable=no-member
    context = {
        "products": products,
        "categories": categories,
        "brands": brands,
        "prices": prices,
    }
    return render(request, "products.html", context)


def product_between_prices(request, price1, price2):
    """A view to show products between prices"""
    products = Product.objects.filter( # pylint: disable=no-member
        price__range=(price1, price2)
    )  # pylint: disable=no-member
    prices = sorted(
        Product.objects.filter(price__range=(price1, price2)).values_list( # pylint: disable=no-member
            "price", flat=True
        )
    )  # pylint: disable=no-member
    categories = Category.objects.all()  # pylint: disable=no-member
    brands = Brand.objects.all()  # pylint: disable=no-member
    context = {
        "products": products,
        "categories": categories,
        "brands": brands,
        "prices": prices,
    }
    return render(request, "products.html", context)


class ProductListApi(ListAPIView):
    """ListApiView definition for Product."""

    queryset = Product.objects.all()  # pylint: disable=no-member
    serializer_class = ProductSerializer


class CategoryListApi(ListAPIView):
    """ListApiView definition for Category."""

    queryset = Category.objects.all()  # pylint: disable=no-member
    serializer_class = CategorySerializer


class BrandListApi(ListAPIView):
    """ListApiView definition for Brand."""

    queryset = Brand.objects.all()  # pylint: disable=no-member
    serializer_class = BrandSerializer


class ProductGiorgioArmani(ListAPIView):
    """ListApiView definition for Product."""

    queryset = Product.objects.filter( # pylint: disable=no-member
        brand__name="Giorgio Armani"
    )  # pylint: disable=no-member
    serializer_class = ProductSerializer
