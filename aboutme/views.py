from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def about_me(request):
    intro=AboutMe.objects.all()
    skills=Skills.objects.all()
    print(skills)
    context={
        'intro':intro,
        'skills':skills
    }
    return render(request,'about_me/about_me.html', context)

