from django import forms
from django.shortcuts import get_object_or_404
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]  # for loop that adds items to a list (id, firendly_name)

        self.fields['category'].choices = friendly_names  # update category field to use friendly names instead of id
        for field_name, field in self.fields.items():  # set classes on the fields 
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        exclude = ('approved',)

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
