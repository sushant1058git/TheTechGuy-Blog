from urllib import request
from django.core import files
from django.shortcuts import render

# Create your views here.
import blogapp
from django import views
from django.core import paginator
from django.http import HttpResponseRedirect
from django.db.models.fields import EmailField
from django.shortcuts import render, redirect,get_object_or_404
from django.views import View
from .models import Blog, Catagory,Tag, EmailSignUp,Comment
from django.core.paginator import Paginator
from django.db.models import Count 
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
import time
# Import mimetypes module
import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse


class HomeView(View):
    def get(self,request,*args,**kwargs):
            featured_obj = Blog.objects.all().filter(status='active', visible=True, featured=True).order_by('-id')[:6]
            post_obj = Blog.objects.all().filter(status='active', visible=True).order_by('-id')
            popular_list = Blog.objects.all().filter(status='active', visible=True,visit_count__gte=50).order_by('-visit_count')[:6]
            # As per Templates Views
            first_post = featured_obj.first()
            s_post = featured_obj[1]
            last_post = featured_obj[2:]
            category=Catagory.objects.all()
            
            # '''Paginator'''
            # paginator = Paginator(post_obj, 3)
            # page_number = request.GET.get('page')
            # page_obj = paginator.get_page(page_number)
                    
            context={
                'post':post_obj,
                # 'post':page_obj,
                'f_post':featured_obj,
                'first':first_post,
                's_post':s_post,
                'last_post':last_post,
                'category':category,
                'popular_list':popular_list
                
            }
            return render(request, 'home/index.html',context)
        

# single blog views
class SingleBlogView(View):
    def get(self,request,id,*args,**kwargs):
        try:
            post_obj = get_object_or_404(Blog, id=id)
            post_obj.visit_count = post_obj.visit_count + 1
            post_obj.save()
            releted_post = Blog.objects.filter(author=post_obj.author).exclude(id=id).order_by('-id')[:4]
            # As per templates views 
            first_post = releted_post.first()
            last_post  = releted_post[1:]
            
            context ={
                'post':post_obj,
                'r_post':releted_post,
                'first':first_post,
                'last':last_post
            }
            return render(request,'blogs/post/single_blog.html', context)
        except:
            return render(request,'404.html')


# Catagory View
class CatagoryView(View):
    def get(self,request,slug,*args,**kwargs):
        catagory_obj = get_object_or_404(Catagory, slug=slug)
        #post = catagory_obj.blog_set.all().order_by('-id')
        try:
            post = Blog.objects.filter(catagories= catagory_obj,\
                status='active',visible=True)\
                .order_by('-created_at')
            popular = Blog.objects.filter(catagories= catagory_obj,\
                status='active',visible=True)\
                .annotate(post_count=Count('visit_count'))\
                .order_by('-visit_count')
            # as Per templates views
            featured_post = popular.first()
            popular_post = popular[1:6]
            # Pagination 
            paginator = Paginator(post, 3)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context ={
                'catagory':catagory_obj,
                'post':page_obj,
                'pop':popular_post,
                'f_post':featured_post,
            }
            return render(request,'blogs/category/category.html', context )
        except:
            return render(request,'404.html')

# tag View
class TagView(View):
    def get(self,request,id,*args,**kwargs):
        tag_obj = get_object_or_404(Tag, id=id)
        post = tag_obj.blog_set.all().order_by('-id')
        tag_count = post.count()
        context={
            'tag':tag_obj,
            'post':post,
            'tag_count':tag_count
        }
        return render(request,'home/tag.html',context)

# Subscribe Views
class SubsCribe(View):
    def post(self, request,*args,**kwargs):
        sub_obj = request.POST.get('subscribe')
        email = EmailSignUp.objects.filter(email=sub_obj)
        if email :
            messages.success(request,'You are already Subscribed , Thanks!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            subscribe = EmailSignUp.objects.create(email=sub_obj)
            subscribe.save()
            messages.success(request,'Thanks for Subscribing')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# search Views
class SearchView(View):
    def get(self,request,*args,**kwargs):
        search = request.GET['q']
        post = Blog.objects.filter(status='active',visible=True)
        if len(search) > 100:
            posts = post.none()
        else:
            posts = post.filter(
                Q(title__icontains=search) |
                Q(catagories__name__icontains=search) |
                Q(detail__icontains = search)
                
            )
        context ={
            'post':posts,
            'search':search
        }
        return render(request,'home/search.html', context)

# Comments View
class CommentView(View):
    def post(self,request,id, *args,**kwargs):
        post = get_object_or_404(Blog,id=id)
        name = request.POST.get('name')
        body = request.POST.get('body')
        comment_obj = Comment(post=post,name=name,body=body)
        comment_obj.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def test(request):
    catagory_obj = Catagory.objects.all()
    cat = Catagory.objects.all().count()
    lent = len(catagory_obj)
    #post = Catagory.blog_set.count()
    #post = Blog.objects.filter(catagories__icontains = catagory_obj).count()

    # src = https://able.bio/rhett/how-to-order-by-count-of-a-foreignkey-field-in-django--26y1ug1
    
    post = Catagory.objects.all() \
        .annotate(post_count=Count('blog'))\
        .order_by('-post_count')
    context = {
        'catagory':catagory_obj,
        'cat':cat,
        'lent':lent,
        'post':post
        
        
    }
    return render(request,'test.html', context)


    
def error404(request,exception):
    return render (request,'404.html')
    