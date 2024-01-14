from django.shortcuts import render
from . forms import StudentForm
# Create your views here.

def index(request):
    std=StudentForm()

    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data)
    else :
        form=StudentForm()
    return render(request, 'app/index.html',{'data':std})
