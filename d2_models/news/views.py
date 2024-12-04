from django.shortcuts import render

from .models import Post, Category, PostCategory
from django.views.generic import ListView, DetailView


class NewsList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'news.html'
    context_object_name = 'news'


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'