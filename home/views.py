from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from products.models import Product
from profiles.models import Testimonial
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    """
    Returns Index Page which displays three highest arted products in cards
     and customer testimonials on a list.
    """
    products = Product.objects.all()
    testimonials = Testimonial.objects.all()

    context = {
        'products': products,
        'testimonials': testimonials,
    }

    return render(request, 'home/index.html', context)
