from django import forms 
from . models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        # fields='__all__'
        exclude=['author']

        # labels={
        #     'title':'Your title  must be within 250 character'
        # }
        # help_texts={
        #     'title':'Do not blank the title'
        # }