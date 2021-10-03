from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Product, Category
from profiles.models import Review
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
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
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
        'products': products,
        'current_categories': categories,
        'product_detail': product_detail,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual product details and thier specific reviews.
    Includes checks to guard against multiple reviews by one user.
    Calculates product rating based on approved reviews.
    """
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(pname=product.id)
    approved_reviews = Review.objects.filter(pname=product.id, approved=True)
    postivie_feedback = Review.objects.filter(pname=product.id, feedback=True,
                                              approved=True)
    negative_feedback = Review.objects.filter(pname=product.id, feedback=False,
                                              approved=True)
    number_of_reviews = 0

    positive = len(postivie_feedback)
    negative = -len(negative_feedback)
    live_rating = product.rating + positive + negative
    if live_rating < 0:
        live_rating = 0
    elif live_rating > 10:
        live_rating = 10
    else:
        live_rating

    number_of_reviews = len(approved_reviews)

    context = {
        'product': product,
        'reviews': reviews,
        'number_of_reviews': number_of_reviews,
        'live_rating': live_rating,
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


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
