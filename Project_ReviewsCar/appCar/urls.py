
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name='indexPage'),
    path('api/country/', views.GetCountryInfoView.as_view()),
]
