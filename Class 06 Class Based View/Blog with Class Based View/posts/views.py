from django.shortcuts import render,redirect
from . forms import PostForm,CommentForm
from . models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView,LogoutView
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



# ---Class Based View ----

#Add Post Create View
@method_decorator(login_required,name='dispatch')
class AddPostCreateView(CreateView):
    model=Post
    form_class=PostForm
    template_name='posts/add_post.html'
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super(AddPostCreateView,self).form_valid(form)
    

#EditPost using Class Based View
@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model=Post
    form_class=PostForm
    template_name='posts/add_post.html'
    pk_url_kwarg='id'
    success_url=reverse_lazy('profile')


# Delete a post using delete view
@method_decorator(login_required,name='dispatch')
class DeleteView(DeleteView):
    model=Post
    # form_class=PostForm
    template_name='posts/delete_post.html'
    success_url=reverse_lazy('profile')
    pk_url_kwarg='id'


# User login using class based view
    


#Detail view using detail View 
    
class DetailPostView(DetailView):
    model=Post
    pk_url_kwarg='id'
    template_name='posts/details.html'
    success_url=reverse_lazy('detail_post')


    def post(self,request,*args,**kwargs):
        comment_form=CommentForm(data=self.request.POST)
        post=self.get_object()

        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
        return self.get(request,*args,**kwargs)
    

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        post=self.object 
        comments=post.comments.all() 
        comment_form=CommentForm()
        context['comments']=comments 
        context['comment_form']=comment_form
        return context
