from django.db import models

# Create your models here.

class student(models.Model):

    name=models.CharField(max_length=30)
    Roll=models.IntegerField(primary_key=True)
    address=models.TextField()
    FatherName=models.TextField(default='Wali')

    def __str__(self) -> str:
        return  f"{self.Roll} : {self.name}"
