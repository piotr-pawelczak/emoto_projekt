from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='fuel-home'),
    path('e95/', views.e95_price, name='e95_price'),
    path('e98/', views.e98_price, name='e98_price'),
    path('on/', views.on_price, name='on_price'),
    path('lpg/', views.lpg_price, name='lpg_price'),
]
