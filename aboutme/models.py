import email
from django.db import models

# Create your models here.
class AboutMe(models.Model):
    about=models.TextField(max_length=500, null=True,blank=True)
    name=models.CharField(max_length=30)
    dob=models.DateField()
    school=models.CharField(max_length=50,blank=True,null=True)
    college=models.CharField(max_length=50,blank=True,null=True)
    degree=models.CharField(max_length=100,null=True,blank=True)
    experience=models.CharField(max_length=50,null=True,blank=True)
    phone=models.CharField(max_length=12)
    email=models.EmailField(max_length=50,blank=True,null=True)
    current_address=models.TextField(max_length=100,blank=True, null=True)
    permanent_address=models.TextField(max_length=300,null=True,blank=True)
    
    
class Skills(models.Model):
    languages=models.CharField(max_length=50,null=True,blank=True)
    webdesign=models.CharField(max_length=50,null=True,blank=+True)
    libraries=models.CharField(max_length=50,null=True,blank=+True)
    databases=models.CharField(max_length=50,null=True,blank=+True)
    framework=models.CharField(max_length=50,null=True,blank=+True)
    ide=models.CharField(max_length=50,null=True,blank=+True)
    versioncontrol=models.CharField(max_length=50,null=True,blank=+True)
    
    
class WorkExp(models.Model):
    comapny_name=models.CharField(max_length=50,null=True,blank=True)
    join_date=models.DateField(null=True,blank=True)
    end_date=models.DateField(null=True, blank=True)
    project_title=models.CharField(max_length=100)
    project_details=models.TextField(max_length=200,null=True, blank=True)
    designation=models.CharField(max_length=50)
    
    def __str__(self):
        return self.comapny_name
    
class PersonalProjects(models.Model):
    project_name=models.CharField(max_length=200)
    project_summary=models.TextField(max_length=500, null=True,blank=True)
    technologies_used=models.ForeignKey(Skills,on_delete=models.CASCADE)
    

class SocialLinks(models.Model):
    github=models.URLField(blank=True, null=True)
    facebook=models.URLField(blank=True, null=True)
    linkdln=models.URLField(blank=True, null=True)
    instagram=models.URLField(blank=True, null=True)
    youtube=models.URLField(blank=True, null=True)
    twitter=models.URLField(blank=True, null=True)
    
    

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='Name')
    email = models.EmailField(null=True)
    messages = models.TextField()
    subject = models.CharField(max_length=200, null=True, verbose_name='Subjects' )

    def __str__(self):
        return self.email
        
