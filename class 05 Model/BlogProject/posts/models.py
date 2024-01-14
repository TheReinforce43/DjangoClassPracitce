from django.db import models
from categories.models  import category
from authors.models import author 
# Create your models here.

class post(models.Model):

    title=models.CharField(max_length=255)
    content=models.TextField()
    category=models.ManyToManyField(to=category)
    author=models.ForeignKey(to=author,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
