from django.contrib import admin
from .models import Categoria, Post

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields =('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields =('created', 'updated')
    prepopulated_fields = {'slug': ('titulo',)}

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)