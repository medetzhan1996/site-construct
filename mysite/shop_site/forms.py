from django import forms
from .models import Сategory


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Сategory
        fields = ['title']
