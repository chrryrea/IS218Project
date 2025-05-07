from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'rating', 'comment']
        widgets = {
            'rating': forms.RadioSelect(),
            'comment': forms.Textarea(attrs={'rows': 4})
        }
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'rating': 'Rating (1-5 stars)',
            'comment': 'Your Review'
        }

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        max_value=10,
        initial=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput()
    )