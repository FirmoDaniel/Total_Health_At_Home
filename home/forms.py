from django import forms
from .models import Testimonial


class TestimonialForm(forms.ModelForm):

    class Meta:
        model = Testimonial
        exclude = ('approved',)

    def __init__(self, *args, **kwargs):
        super(TestimonialForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
