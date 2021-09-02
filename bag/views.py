from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def view_bag(request):
    """
    Returns shopping bag
    """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ add item to the bag """
    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')  # redirect user back to previous page after adding product to bag
    bag = request.session.get('bag', {})  # check if bag in session, create it if not

    bag[item_id] = {product.name}