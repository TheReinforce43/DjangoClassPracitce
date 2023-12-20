from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'app/index.html')

def result(request):
    name=None
    email=None
    if request.method == 'POST':
        name=request.POST.get('UserName')
        email=request.POST.get('UserEmail')
        print('Name ',name)
        print('Email ',email)
        return render(request,'app/result.html',{'userName': name,'UserEmail': email})
    else :
        return render(request,'app/result.html',{'userName': name,'UserEmail': email})

def form(request):
    # print(request.POST)
    return render(request,'app/form.html')
