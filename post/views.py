from django.shortcuts import render
from .models import Post


# Create your views here.

def home(request):

    return render(request, 'post/home.html')
