from django.db import models

# Create your models here.

class author(models.Model):

    name=models.CharField(max_length=50)
    bio=models.TextField()
    phone_no=models.CharField(max_length=15)

    def __str__(self):
        return f'{self.name}'
    
