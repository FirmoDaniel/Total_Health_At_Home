from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
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
        'testimonials': testimonials,
    }

    return render(request, 'home/index.html', context)


@login_required
def add_testimonial(request):
    """ Add a Testimonial to the store """
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added Testimonial for review.')
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Failed to add Testimonial. Please ensure your form is valid.')
    else:
        form = TestimonialForm(initial={'username': request.user})  # prepop the user name in form
    template = 'home/add_testimonial.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_testimonial(request, testimonial_id):
    """ Edit a testimonial """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Testimonial!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to update Testimonial. Please ensure the form is valid.')
    else:
        form = TestimonialForm(instance=testimonial)
        messages.info(request, f'You are editing {testimonial.username}(s) testimonial')

    template = 'home/edit_testimonial.html'
    context = {
        'form': form,
        'testimonial': testimonial,
    }

    return render(request, template, context)
