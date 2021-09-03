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
    quantity = 1  # default quantity of 1

    if item_id in list(bag.keys()):  # checks if item already in bag
        messages.info(request, f'{product.name} already in your bag')
        return redirect('products')
    else:
        bag[item_id] = quantity  # this can be product.name 
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    print(request.session['bag'])  # print to console for verification
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    product = get_object_or_404(Product, pk=item_id)

    try:
        if request.POST:
            bag = request.session.get('bag', {})
            bag.pop(item_id)
            messages.warning(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
