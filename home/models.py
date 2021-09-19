from django.db import models

# Create your models here.


class Testimonial(models.Model):

    username = models.CharField(max_length=64, null=False, blank=False)
    description = models.TextField(null=False, blank=False, default='The site helped me achieve my goals')
    approved = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.username
