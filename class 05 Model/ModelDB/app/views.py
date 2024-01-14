from django.shortcuts import render,redirect
from . import models 

# Create your views here.


def index(request):
    student=models.student.objects.all()
    print(student)
    return render(request, 'app/index.html',{'student':student})


def delete_student(request,Roll):
    student=models.student.objects.get(pk=Roll).delete()
    print(student)
    return redirect('app')
    # student=models.student.objects.all()
   
    # return render(request,'app/index.html',{'student':student})

