from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Product, Category

# Create your views here.


def all_products(request):
    """ Returns Prodcts page and includes sorting """

    products = Product.objects.all()  # returns all products
    categories = None

    if request.GET:  # sorting by categories
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')  # splits query into a list at the comma
            products = products.filter(category__name__in=categories)  # filter products by those with matching category name
            categories = Category.objects.filter(name__in=categories)  # filter categories down to ones existing in the url to show what categorys are veing viewed by friendly name

    context = {
        'products': products,  # products variable sent to template via context
        'current_categories': categories
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
