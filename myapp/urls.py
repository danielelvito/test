 

from django.urls import path
from . import views
from .user_form_view import register

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('create/', views.item_create, name='item_create'),
    path('register/', register, name='register'),
]