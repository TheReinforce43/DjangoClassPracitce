from django.shortcuts import render,redirect
from . forms import CategoryForm
# Create your views here.

def add_category(request):
    # return render(request,'categories/add_category.html')

    if request.method=='POST':

        categoryform=CategoryForm(request.POST)
        if categoryform.is_valid():
            categoryform.save()
            return redirect('home')
    else :
        categoryform=CategoryForm()

    return render(request,'categories/add_category.html',{'form':categoryform})
   