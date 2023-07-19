"""Home views."""
from django.shortcuts import render
from store.models import Product, Category, Brand

# the html file is in the templates folder like this:
# mysite\home\templates\home\index.html
def index(request):
    """load index.html"""
    products = Product.objects.all() # pylint: disable=no-member
    prices = Product.objects.all().values_list("price", flat=True) # pylint: disable=no-member
    #sort by price
    prices = sorted(prices)
    categories = Category.objects.all() # pylint: disable=no-member
    brands = Brand.objects.all() # pylint: disable=no-member
    context = {
        'title': 'Home',
        'products': products,
        'categories': categories,
        'brands': brands,
        'prices': prices,
    }
    return render(request, 'index.html', context)
