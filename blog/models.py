from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=80)
    slug = models.SlugField(max_length=200, unique=True)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='blog', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated',)
        verbose_name = 'post'
        verbose_name_plural = 'posts'
    def __str__(self):
        return self.titulo
