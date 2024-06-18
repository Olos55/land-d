from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lands/', views.land_list, name='land_list'),
]
