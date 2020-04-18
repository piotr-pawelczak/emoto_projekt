from django.urls import path, include
from . import views

urlpatterns = [
    path('all/', views.home, name='achievements-home'),
    path('todo/', views.not_achieved, name='achievements-todo'),
    path('done/', views.achieved, name='achievements-done'),
]
