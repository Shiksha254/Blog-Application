from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django .contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import Post, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
# def home(request):
#     return render(request, 'home.html')
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html' 
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)  
    # fields = '__all__' 
    success_url = reverse_lazy('home')

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields= ['title', 'content', 'author']    

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    likes =False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article_details', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['id']

class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post.total_likes 
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():  
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
    
def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have Registered Successfully!! WELCOME"))
            return redirect('home')
        else:
          messages.success(request, ("Whoops! There was a problem REgistering, Please try again..."))
          return redirect('register')  

    return render(request, 'register.html', {'form':form})
    


def login_user(request):
    if request.method == "POST":
        username =request.POST['username']
        password =request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged In...."))
            return redirect('home')
        else:
            messages.success(request, ("There was an Error, Please Try Again..."))
            return redirect('home')
    else:
       return render(request, 'login.html')
    

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out...."))
    return redirect('home')
