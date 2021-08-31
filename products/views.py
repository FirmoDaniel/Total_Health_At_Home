from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """ Returns Prodcts page and includes sorting """

    products = Product.objects.all()  # returns all products

    context = {
        'products': products,  # products variable sent to template via context
    }

    return render(request, 'products/products.html', context)
