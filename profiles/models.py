from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import Product

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()


class Testimonial(models.Model):

    username = models.CharField(max_length=64, null=False, blank=False)
    description = models.TextField(null=False, blank=False, default='The site helped me achieve my goals')
    approved = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.username

#  REVIEW MODEL

class Review(models.Model):

    username = models.CharField(max_length=64, null=False, blank=False)
    name = models.CharField(max_length=64, null=False, blank=False)
    description = models.TextField(null=False, blank=False, default='The site helped me achieve my goals')
    feedback = models.BooleanField(default=False, null=False, blank=False)
    approved = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.username