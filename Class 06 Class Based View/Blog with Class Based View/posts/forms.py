from django import forms 
from . models import Post
from . import models

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

class CommentForm(forms.ModelForm):

    class Meta:

        model=models.Comment

        fields=['name','email','body']


        