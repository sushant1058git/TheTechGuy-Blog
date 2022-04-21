import re
from sre_parse import ESCAPES
# from tkinter import ss
from django.shortcuts import redirect, render
from .models import *
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
from Blog.settings import *
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from Blog.settings import EMAIL_HOST_USER
import socket
1


# Create your views here.
def about_me(request):
    intro=AboutMe.objects.all()
    skills=Skills.objects.all()
    exp=WorkExp.objects.all()[::-1]
    education=Education.objects.all().order_by('-year')
    source_map=Map.objects.all().first()
    urls=SocialLinks.objects.all()
    proj_image=ProjectImage.objects.all()
        
    context={
        'intro':intro,
        'skills':skills,
        'exp':exp,
        'education':education,
        'source_map':source_map,
        'urls':urls,
        'proj_image':proj_image
    }
    return render(request,'about_me/about_me.html', context)


def download_resume(request):
    about_me=AboutMe.objects.all().order_by('-id').first()
    file_name=about_me.resume
    fs = FileSystemStorage()
    filename = str(BASE_DIR)+'/media/'+ str(file_name)
    if fs.exists(filename):
        with fs.open(filename) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Sushant_Resume.pdf"'
            return response
    else:
        return HttpResponseNotFound('The requested pdf was not found in our server.')
    

            
def blog_contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        subject=request.POST.get('subject')
        contact_details=Contact.objects.create(name=name,email=email,messages=message,subject=subject)
        contact_details.save()
        socket.gethostbyname("")
        try:
            from_email = EMAIL_HOST_USER
            to_email = [contact_details.email,]
            contact_message = f"Hey {name}, Thanks for Contacting. I will get back to you soon"
            contact_subject ="Thanks for Contacting !!"

            send_mail(
                contact_subject,
                contact_message,
                from_email,
                to_email,
                fail_silently=False,
            )
            to_email = [EMAIL_HOST_USER,]
            contact_message = f"Hey TheTechGuy, you have new message.\nName: {name}.\nSubject:{subject}\nMessage:{message}"
            contact_subject ="New message !!"

            send_mail(
                contact_subject,
                contact_message,
                from_email,
                to_email,
                fail_silently=False,
            )
            
            messages.success(request,"Thanks for contacting.!!")
            

        except BadHeaderError:
            return HttpResponse('Something Went Wrong!!')
        return redirect('about_me')
    else:
        return render(request,'about_me/about_me.html')