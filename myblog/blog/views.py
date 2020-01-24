from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.views.generic import View
from django.urls import reverse

from .models import Post, Tag
from .utils import *
from .forms import TagForm, PostForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from django.db.models import Q

def posts_list(requests):
    search_query = requests.GET.get('search','')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains = search_query) | Q(body__icontains = search_query))
    else:
        posts = Post.objects.all()
    
    
    paginator = Paginator(posts, 2)


    page_number = requests.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    prev_url = ''
    next_url = ''

    if page.has_previous():
        prev_url = f'?page={page.previous_page_number()}'
    
    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
    

    context = {
        'page_object' : page,
        'is_paginated' : is_paginated,
        'prev_url' : prev_url,
        'next_url' : next_url,
    }


    return render(requests, 'blog/index.html', context = context)


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


