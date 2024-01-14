from django.shortcuts import render,redirect

from . forms import PostForm

from . models import Post

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def add_post(request):
    # return render(request, 'posts/add_post.html')

    if request.method=='POST':
        postform=PostForm(request.POST)

        if postform.is_valid():
            # postform.cleaned_data['author']=request.user
            postform.instance.author=request.user
            postform.save()
            return redirect('home')
    else :
        postform=PostForm()
    return render(request, 'posts/add_post.html',{'form':postform,'type':'POST'})


@login_required
def edit_post(request,id):

    post_id=Post.objects.get(pk=id)
    post_instance=PostForm(instance=post_id)

    if request.method=='POST':
        post_instance=PostForm(request.POST,instance=post_id)
        if post_instance.is_valid():
            post_instance.instance.author=request.user
            post_instance.save()
            return redirect('home')
    
    return render(request,'posts/add_post.html',{'form':post_instance} )


@login_required
def delete_post(request,id):
    post_id=Post.objects.get(pk=id)
    post_id.delete()
    return redirect('home')




