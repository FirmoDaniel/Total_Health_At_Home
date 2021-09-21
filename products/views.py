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
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure your form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
