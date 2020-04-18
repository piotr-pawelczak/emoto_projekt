from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.stats, name='stats-home'),
]
