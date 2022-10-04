from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('<slug:slug>/', views.PostDetail.as_view(), name="post"),
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
]