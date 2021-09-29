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
        self.user = kwargs.pop('user')  # get user to check if superuser
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
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')  # get user to check if superuser
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['pname'].widget.attrs['hidden'] = True
        self.fields['pname'].label = False
        self.fields['name'].widget.attrs['readonly'] = True

        feedback_choices = (
            (True, 'I liked it'),
            (False, 'No Likey'),
        )
        self.fields['feedback'].widget = forms.RadioSelect(
            choices=feedback_choices, attrs={'required': 'required'})
        if self.user.is_superuser:
            self.fields['approved'].widget.attrs['disabled'] = False
        else:
            self.fields['approved'].widget.attrs['disabled'] = True
