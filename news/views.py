from django.shortcuts import render

from .models import Post, Category, PostCategory
from django.views.generic import ListView


class NewsList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'news.html'
    context_object_name = 'news'

