from django.shortcuts import redirect, render

# Create your views here.
def about_me(request):
    return render(request,'about_me/about_me.html')