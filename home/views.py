from django.shortcuts import render

# Create your views here.


def index(request):
    """ Returns home page """
    return render(request, 'home/index.html')
