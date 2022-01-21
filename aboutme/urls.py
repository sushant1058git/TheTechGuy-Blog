from django.urls import path
from django.views.generic.base import View
from . import views

urlpatterns = [
    path('aboutme/', views.about_me, name='about_me'),
    
]