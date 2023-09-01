from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'serial_number', 'description', 'main_image', 'item_images')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-3'}),
            'main_image': forms.Select(attrs={'class': 'form-control mb-3'}),
            'item_images': forms.SelectMultiple(attrs={'class': 'form-control mb-3'}),
        }

