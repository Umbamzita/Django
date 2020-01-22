from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.views.generic import View
from django.urls import reverse

from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm

from django.contrib.auth.mixins import LoginRequiredMixin

def posts_list(requests):
    posts = Post.objects.all().order_by('-date_pub')
    return render(requests, 'blog/index.html', context = {'posts' : posts})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True

class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    update_form_model = TagForm
    template = 'blog/tag_update.html'
    raise_exception = True

class TagDelete(LoginRequiredMixin, ObjectDeleteMixin,View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect_url = 'tags_list_url'
    raise_exception = True




class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'

class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    form_model = PostForm
    template = 'blog/post_create.html'
    raise_exception = True

class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    update_form_model = PostForm
    template = 'blog/post_update.html'
    raise_exception = True

class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect_url = 'posts_list_url'
    raise_exception = True


def tags_list(requests):
    tags = Tag.objects.all()
    return render(requests, 'blog/tags_list.html', context = {'tags' : tags})




# class TagDelete(View):
#     def get(self, requests, slug):
#         tag = Tag.objects.get(slug__iexact = slug)
#         return render(requests, 'blog/tag_delete.html', context = {'tag' : tag})
    
#     def post(self, requests, slug):
#         tag = Tag.objects.get(slug__iexact = slug)
#         tag.delete()
#         return redirect(reverse('tags_list_url'))


