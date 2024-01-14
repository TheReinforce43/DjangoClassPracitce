from django.db import models
from categories.models import Category
from authors.models import Author
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    category=models.ManyToManyField(to=Category)
    author=models.ForeignKey(to=Author,on_delete=models.CASCADE) 

    def __str__(self) -> str:
        return self.title