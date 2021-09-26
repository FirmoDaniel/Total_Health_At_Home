from django import forms
from .models import UserProfile
from .models import Testimonial, Review
from products.models import Product


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_diet': 'Specify Diet (Vegan//Omnivore etc)',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'profile-update-form'
            self.fields[field].label = False


class TestimonialForm(forms.ModelForm):

    class Meta:
        model = Testimonial
        fields = '__all__'
        


    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(TestimonialForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        if self.user.is_superuser:
            self.fields['approved'].widget.attrs['disabled'] = False
        else:
            self.fields['approved'].widget.attrs['disabled'] = True


#  REVIEW FORM

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        exclude = ('approved',)

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        product = Product.objects.all()  # setting product variable
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['name'].initial = 'product.name'  # trying to set product.id as initial 
