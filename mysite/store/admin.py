"""importing models from models.py and registering them in admin site"""
from django.contrib import admin

# Register your models here.
from .models import (
    Client,
    Product,
    Order,
    OrderItem,
    Cart,
    WishList,
    Category,
    Brand,
    ProductCategory,
    ProductBrand,
)

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(WishList)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductCategory)
admin.site.register(ProductBrand)
