from django.shortcuts import render
from products.models import Product
from .models import Testimonial
from django.contrib.auth.decorators import login_required
from .forms import TestimonialForm

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


@login_required
def add_testimonial(request):
    """ Add a Testimonial to the store """
    form = TestimonialForm(initial={'username': request.user})  # prepop the user name in form
    template = 'home/add_testimonial.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
