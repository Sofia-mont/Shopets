from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView

from .models import Post, Categoria
# Create your views here.

def blog(request):
    posts = Post.objects.all()
    categoria = Categoria.objects.all()
    return render(request, "blog/blog.html", {'posts':posts, 'categorias':categoria})

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)
    return render(request, "blog/categorias.html", {'categoria':categoria, "posts":posts})