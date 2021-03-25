from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('tour-packages', views.tours, name="tours"),
    path('tour-packages/<str:slug>', views.singleTours, name="singleTours")
]