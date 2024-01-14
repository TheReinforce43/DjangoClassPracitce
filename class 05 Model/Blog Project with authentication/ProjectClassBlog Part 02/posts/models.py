from django.db import models
from categories.models import Category

from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    category=models.ManyToManyField(to=Category)
    register=models.ForeignKey(to=User,on_delete=models.CASCADE,default=None,null=True)

    def __str__(self) -> str:
        return self.title