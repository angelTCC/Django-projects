from django import forms
from .models import Book

class InputForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 
            'author',
            'published_date',
            'description'
            ]
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),  # Render as an HTML date picker
        }

