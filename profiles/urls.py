from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('add_testimonial/', views.add_testimonial, name='add_testimonial'),
    path('edit_testimonial/<int:testimonial_id>/', views.edit_testimonial, name='edit_testimonial'),
    path('delete_testimonial/<int:testimonial_id>/', views.delete_testimonial, name='delete_testimonial'),
]
