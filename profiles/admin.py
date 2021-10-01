from django.contrib import admin
from .models import Testimonial, Review

# Register your models here.


class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'description',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'pname',
        'name',
        'description',
        'feedback',
        'approved',
    )


admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Review, ReviewAdmin)
