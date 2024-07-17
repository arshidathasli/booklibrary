from django import forms

from .models import Book,Author

class AuthorForm(forms.ModelForm):

    class Meta:

        model=Author
        fields=['name']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'author', 'image','quantity'] 

        widgets={
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the book name'}),
            'author':forms.Select(attrs={'class':'form-control','placeholder':'Enter the author name'}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the price'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Upload'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the quqntiry'}),
        }