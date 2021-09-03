from django.shortcuts import (
    render, redirect, HttpResponse, get_object_or_404, reverse)
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """
    Returns shopping bag
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ add item to the bag,  """
    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')  # redirect user back to previous page after adding product to bag
    bag = request.session.get('bag', {})  # check if bag in session, create it if not

    if item_id in list(bag.keys()):  # checks if item already in bag, allowing only quantity of 1 per bag
        messages.info(request, f'{product.name} already in your bag')
        return redirect('products')
    else:
        bag[item_id] = product.name  # may need ot chanage this to quantity for product count later
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
