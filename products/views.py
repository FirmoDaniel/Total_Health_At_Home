from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Product, Category

# Create your views here.


def all_products(request):
    """ Returns Prodcts page and includes sorting """

    products = Product.objects.all()  # returns all products
    categories = None
    sort = None
    direction = None

    if request.GET:
        # sorting by product details (day,home,night)
        if 'sort' in request.GET:
            sortkey = request.GET['sort']  # set a variable equal to the sort term in the GET request
            sort = sortkey
            if sortkey == 'name':  # annotation > handle case sensitivity
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'  # reverses direction with -1 if direction == desc
            products = products.order_by(sortkey)  # sorts the products by the sortkey
        # sorting by categories
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')  # splits query into a list at the comma
            products = products.filter(category__name__in=categories)  # filter products by those with matching category name
            categories = Category.objects.filter(name__in=categories)  # filter categories down to ones existing in the url to show what categorys are veing viewed by friendly name

    current_sorting = f'{sort}_{direction}'  # to display current sorting to user

    context = {
        'products': products,  # products variable sent to template via context
        'current_categories': categories,
        'current_sorting' : current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
