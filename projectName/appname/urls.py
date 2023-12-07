from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('contacts/', views.contacts),
    path('codepractice/', views.codepractice),
    path('marketplace/', views.marketplace),
]