from django import forms 
from . models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

        labels={
            'name':'Add the category of Blog'
        }
        help_texts={
            'name':'Category name can\'t cross 100 characters'
        }
    
