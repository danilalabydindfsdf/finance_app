from django import forms
from .models import FoodProducts


class FoodProductsForm(forms.ModelForm):
    class Meta:
        model = FoodProducts
        fields = ['title', 'amount', 'price']