from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Testimonial
from .forms import TestimonialForm

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order, OrderLineItem

from products.models import Product


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    testimonials = Testimonial.objects.all()  # get all testimonials
    user_testimonials = Testimonial.objects.filter(username=request.user)  # get only testimonial posted by current user
    order = Order.objects.all()

    if request.method == 'POST':
        form_UserProfileForm = UserProfileForm(request.POST, instance=profile)
        if form_UserProfileForm.is_valid():
            form_UserProfileForm.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid')
    else:
        form_UserProfileForm = UserProfileForm(instance=profile)
    orders = profile.orders.all()

   

    template = 'profiles/profile.html'
    context = {
        'form_UserProfileForm': form_UserProfileForm,
        'orders': orders,
        'on_profile_page': True,
        'testimonials': testimonials,
        'user_testimonials': user_testimonials,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'  # uses this template to generate order history via order_number
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


#  TESTIMONIALS

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
