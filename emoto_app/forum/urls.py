from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='forum-home'),
    path('posts/', views.posts, name='forum-posts')
]
