from django.urls import path
from django.views.generic.base import View
from . import views

urlpatterns = [
    path('', views.about_me, name='about_me'),
    path('download/',views.download_resume, name='download_resume'),
    path('blog_contact/', views.blog_contact, name='blog_contact'),
    
]