from django.db import models

# Create your models here.

class StudentModel(models.Model):
    Roll=models.IntegerField(primary_key=True)
    Name=models.CharField( max_length=50)
    Qualification=models.CharField( max_length=50)
    Address=models.TextField()

    def __str__(self) -> str:
        return f'name: {self.Name}'
    