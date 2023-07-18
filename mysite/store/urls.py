"""set up the urls for the store app"""
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # VIEWS
    path("", views.all_products, name="products"),
    path(
        "category/<str:category_name>/",
        views.product_per_category,
        name="product_per_category",
    ),
    path("brand/<str:brand_name>/", views.product_per_brand, name="product_per_brand"),
    path("price/<int:price>/", views.product_by_price, name="product_by_price"),
    # Home page
    path("home/", include("home.urls")),
    # API VIEWS
    path("api/products/", views.ProductListApi.as_view(), name="product_list_api"),
    path("api/categories/", views.CategoryListApi.as_view(), name="category_list_api"),
    path("api/brands/", views.BrandListApi.as_view(), name="brand_list_api"),
    path(
        "api/products/giorgioarmani/",
        views.ProductGiorgioArmani.as_view(),
        name="product_giorgioarmani",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
