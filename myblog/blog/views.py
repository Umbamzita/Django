from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def posts_list(requests):
    posts = Post.objects.all()
    return render(requests, 'blog/index.html', context = {'posts' : posts})

