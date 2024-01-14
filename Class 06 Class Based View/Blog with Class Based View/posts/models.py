from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    category=models.ManyToManyField(to=Category)
    author=models.ForeignKey(to=User,on_delete=models.CASCADE) 
    image=models.ImageField(upload_to='posts/media/uploads/',blank=True,null=True)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"comments by {self.name}"
    