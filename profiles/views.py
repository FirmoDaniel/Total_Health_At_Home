from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Testimonial, Review
from .forms import TestimonialForm, ReviewForm

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order, OrderLineItem

from products.models import Product


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    testimonials = Testimonial.objects.all()
    user_testimonials = Testimonial.objects.filter(username=request.user)
    reviews = Review.objects.all()
    user_reviews = Review.objects.filter(username=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure a valid form.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'testimonials': testimonials,
        'user_testimonials': user_testimonials,
        'reviews': reviews,
        'user_reviews': user_reviews,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """ Display the user's Order History. """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    if not orders:
        messages.warning(request, 'You must have orders to view order history')
        return redirect(reverse('profile'))

    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

#  TESTIMONIALS


@login_required
def add_testimonial(request):
    """ Add a Testimonial to the store """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()
    if not orders:
        messages.warning(request, 'You must have orders to submit a testimonial')
        return redirect(reverse('profile'))

    users_existing_testimonials = Testimonial.objects.filter(username=request.user)
    existing_testimonials = len(users_existing_testimonials)

    if request.method == 'POST':
        form = TestimonialForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added Testimonial for review.')
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Failed to add Testimonial. Please ensure your form is valid.')
    else:
        form = TestimonialForm(initial={'username': request.user},
                               user=request.user)

    template = 'profiles/add_testimonial.html'
    context = {
        'form': form,
        'orders': orders,
        'existing_testimonials': existing_testimonials,
    }

    return render(request, template, context)


@login_required
def edit_testimonial(request, testimonial_id):
    """ Edit a testimonial """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('profile'))

    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial,
                               user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Testimonial!')
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Failed to update Testimonial. Please ensure the form is valid.')
    else:
        form = TestimonialForm(instance=testimonial, user=request.user)
        messages.info(request, f'You are editing {testimonial.username}(s) testimonial')

    template = 'profiles/edit_testimonial.html'
    context = {
        'form': form,
        'testimonial': testimonial,
    }

    return render(request, template, context)


@login_required
def delete_testimonial(request, testimonial_id):
    """ Delete a Testimonial """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('profile'))

    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    testimonial.delete()
    messages.success(request, 'Testimonial deleted!')
    return redirect(reverse('profile'))


#  REVIEWS

@login_required
def add_review(request, product_id):
    """ Render a pre-populated form
    with product id from profile purchased products """
    product = get_object_or_404(Product, pk=product_id)

    lineitems = OrderLineItem.objects.all()
    myorders = lineitems.filter(username=request.user, product=product.id)
    myorders_exist = len(myorders)

    users_existing_reviews = Review.objects.filter(pname=product.id,
                                                   username=request.user)
    existing_reviews = len(users_existing_reviews)

    if request.method == 'POST':
        form = ReviewForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Failed to add Review. Please ensure your form is valid.')
    else:
        if existing_reviews < 1 and myorders_exist > 0:
            form = ReviewForm(initial={'username': request.user,
                                       'pname': product.id,
                                       'name': product.name,
                                       'feedback': 'checked'},
                              user=request.user)
        else:
            messages.error(request, 'You have either not purchased, or have already reviewed, this product')
            return redirect(reverse('profile'))

    template = 'profiles/add_review.html'
    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete a Review """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Review deleted!')
    return redirect(reverse('products'))


@login_required
def edit_review(request, review_id):
    """ Edit a Review """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated Review!')
            return redirect(reverse('profile'))
        else:
            messages.error(request, 'Failed to update Review. Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=review, user=request.user)

    template = 'profiles/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }
    return render(request, template, context)
