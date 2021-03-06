from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


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
        for __, field in self.fields.items():  # set classes on the fields
            field.widget.attrs['class'] = 'generic-form'
