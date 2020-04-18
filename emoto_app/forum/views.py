from django.shortcuts import render
from forum.models import Post

current_speed = 54


def home(request):
    context = {
        'speed': current_speed
    }
    return render(request, 'forum/home.html', context)


def posts(request):
    posts_list = Post.objects.all()
    context = {
        'posts': posts_list
    }
    return render(request, 'forum/posts.html', context)
