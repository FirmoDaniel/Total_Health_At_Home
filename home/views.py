from django.shortcuts import render
from products.models import Product
from .models import Testimonial

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
        'testimonials': testimonials
    }

    return render(request, 'home/index.html', context)
