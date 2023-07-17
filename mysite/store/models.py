"""Models for the store app"""
from django.db import models

# Create your models here.

# Ecommerce for a perfume store
# Entitys: Client,
# Product, Order,
# OrderItem, Cart,
# WishList, Category,
# Brand,
# ProductCategory, ProductBrand


# Client
#   - name
#   - email
#   - password
#   - address
#   - phone
#   - country
#   - city
class Client(models.Model):
    """Model definition for Client."""

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        """Unicode representation of Client."""
        return str(self.name)


# Product
#   - name
#   - description
#   - price
#   - image
#   - category
#   - brand
#   - stock
class Product(models.Model):
    """Model definition for Product."""

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
    stock = models.IntegerField()

    def __str__(self):
        return str(self.name)
# Order
#   - client
#   - date
#   - total
class Order(models.Model):
    """Model definition for Order."""

    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)

# OrderItem
#   - order
#   - product
#   - quantity
#   - total
class OrderItem(models.Model):
    """Model definition for OrderItem."""

    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)

# Cart
#   - client
#   - date
#   - total
class Cart(models.Model):
    """Model definition for Cart."""

    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)


# WishList
#   - client
#   - date
class WishList(models.Model):
    """Model definition for WishList."""

    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


# Category
#   - name
class Category(models.Model):
    """Model definition for Category."""

    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


# Brand
#   - name
class Brand(models.Model):
    """Model definition for Brand."""

    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


# ProductCategory
#   - product
#   - category
class ProductCategory(models.Model):
    """Model definition for Product_category."""
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


# ProductBrand
#   - product
#   - brand
class ProductBrand(models.Model):
    """Model definition for Product_brand."""

    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
