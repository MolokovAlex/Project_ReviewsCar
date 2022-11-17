
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path ('', index),
    path('', views.indexPage, name='indexPage'),
]
