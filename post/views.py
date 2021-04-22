from django.shortcuts import render

from .form import PostForm
from .models import Post


# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'post/home.html', context)


def post_creation(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, "success.html")
    else:
        form = PostForm()
        return render(request, "post/post_creation.html", {"form": form})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post
    }
    return render(request, "post/post_detail.html")
