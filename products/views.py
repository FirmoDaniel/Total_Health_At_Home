from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Product, Category
from django.contrib.auth.decorators import login_required
from .forms import ProductForm

# Create your views here.


def all_products(request):
    """ Returns Prodcts page and includes sorting """

    products = Product.objects.all()  # returns all products
    categories = None
    product_detail = None

    if request.GET:
        # filtering by categories
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')  # splits query into a list at the comma
            products = products.filter(category__name__in=categories)  # filter products by those with matching category name
            categories = Category.objects.filter(name__in=categories)  # filter categories down to ones existing in the url to show what categorys are veing viewed by friendly name
        #  filtering by product details (day,home,night,outdoors)
        if 'night' in request.GET:
            products = products.filter(night__in=products)
            product_detail = 'night'
        if 'day' in request.GET:
            products = products.filter(day__in=products)
            product_detail = 'day'
        if 'home' in request.GET:
            products = products.filter(home__in=products)
            product_detail = 'home'
        if 'outdoors' in request.GET:
            products = products.filter(outdoors__in=products)
            product_detail = 'outdoors'

    context = {
        'products': products,  # products variable sent to template via context
        'current_categories': categories,
        'product_detail': product_detail,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
