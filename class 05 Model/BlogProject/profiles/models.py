from django.db import models
from authors.models import author

# Create your models here.


class profile(models.Model):
    
    name=models.CharField(max_length=255)
    author = models.OneToOneField(author, on_delete=models.CASCADE,default=None)
    about=models.TextField()

    def __str__(self) -> str:
        return self.name