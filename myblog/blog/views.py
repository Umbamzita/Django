from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Tag
from django.views.generic import View
from .utils import ObjectDetailMixin


def posts_list(requests):
    posts = Post.objects.all()
    return render(requests, 'blog/index.html', context = {'posts' : posts})



class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'




def tags_list(requests):
    tags = Tag.objects.all()
    return render(requests, 'blog/tags_list.html', context = {'tags' : tags})

# def tag_detail(requests, slug):
#     tag = Tag.objects.get(slug__iexact = slug)
#     return render(requests, 'blog/tag_detail.html', context = {'tag' : tag})

# def post_detail(requests, slug):
#     post = Post.objects.get(slug__iexact = slug)
#     return render(requests, 'blog/post_detail.html', context = {'post' : post})
