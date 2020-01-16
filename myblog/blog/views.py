from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.views.generic import View

from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm


def posts_list(requests):
    posts = Post.objects.all().order_by('-date_pub')
    return render(requests, 'blog/index.html', context = {'posts' : posts})



class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'

  

class PostCreate(ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create.html'



def tags_list(requests):
    tags = Tag.objects.all()
    return render(requests, 'blog/tags_list.html', context = {'tags' : tags})

