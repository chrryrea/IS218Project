from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.RadioSelect(),
            'comment': forms.Textarea(attrs={'rows': 4})
        }
        labels = {
            'rating': 'Rating (1-5 stars)',
            'comment': 'Your Feedback'
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