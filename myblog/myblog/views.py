from django.shortcuts import render, redirect


def redirect_blog(requests):
    return redirect('posts_list_url', permanent = True)
