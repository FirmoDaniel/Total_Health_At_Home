from django.db import models

# Create your models here.


class Testimonial(models.Model):

    username = models.CharField(max_length=254)
    description = models.TextField()

    def __str__(self):
        return self.username
