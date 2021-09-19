from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add_testimonial/', views.add_testimonial, name='add_testimonial'),
]
