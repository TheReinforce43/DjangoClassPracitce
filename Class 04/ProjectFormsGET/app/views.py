from django.shortcuts import render
from . forms import contactForm

# Create your views here.


def index(request):

    return render(request, 'app/index.html')

def form(request):

    return render(request, 'app/form.html')

# without using cleaned data here
# def DjangoForm(request):
#     FormResult=contactForm(request.POST)
#     if FormResult.is_valid():
#         print(FormResult.cleaned_data)
#     return render(request, './app/DjangoForm.html',{'formResult':FormResult})

# With using cleaned data  

def DjangoForm(request):
   
   if request.method=='POST':
       formResult=contactForm(request.POST,request.FILES)
       if formResult.is_valid():
           file=formResult.cleaned_data['file']
           print(formResult.cleaned_data)

           with open('./app/upload/'+file.name ,'wb+') as destination:
               for chunk in file.chunks():
                   destination.write(chunk)
       else:
           print("Forms Error :",formResult.errors)
   else :
        formResult=contactForm()  
   return render(request,'app/DjangoForm.html',{'formResult':formResult})
    

def result(request):
    # return render(request,'app/result.html')

    if request.method=='POST':
       
       data={
            'name':request.POST.get('name'),
            'email':request.POST.get('email'),
            'selectValue':request.POST.get('select')
        }
       
       return render(request,'app/result.html',context={'data': data})
        # print(name,email,selectValue)
        # return render(request,'app/result.html',{'name':name,'email':email,'selectValue':selectValue})
        
    else :
        return render(request,'app/result.html')

# def result(request):

#     data=dict()

#     if request.method=='POST':
#         data={
#             'name':request.POST.get('name'),
#             'email':request.POST.get('email'),
#             'selectValue':request.POST.get('select')
#         }
#         print(data)
#         return render(request,'app/reuslt.html',data)
#     else:
#         return render(request,'app/reuslt.html',data) 
