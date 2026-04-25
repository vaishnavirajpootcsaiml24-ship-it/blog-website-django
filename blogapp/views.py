from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm, UserRegisterForm
from django.contrib import messages


def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            posts = Post.objects.all().order_by('-created_at')
        else:
            posts = Post.objects.filter(author=request.user).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')

    return render(request, 'blogapp/home.html', {'posts': posts})


@login_required
def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)   # ✅ FIX 1
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']   # ✅ FIX 2
            messages.success(request, f'Account Created for {username}! You can now log in')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'blogapp/signup.html', {'form': form})


def create_post(request):
    pass


def post_detail(request):
    pass