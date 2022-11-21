
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexPage, name='indexPage'),
    path('api/country/', views.GetCountryInfoView.as_view()),
    path('api/manuf/', views.GetManufInfoView.as_view()),
    path('api/car/', views.GetCarInfoView.as_view()),
    path('api/comment/', views.GetCommentInfoView.as_view()),
]
