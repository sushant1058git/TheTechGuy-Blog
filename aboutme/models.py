import email
from re import T
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class AboutMe(models.Model):
    about=RichTextField(null=True,blank=True)
    name=models.CharField(max_length=30)
    dob=models.DateField()
    sec_school=models.CharField(max_length=50,blank=True,null=True)
    perc_in_sec_school=models.CharField(max_length=100,blank=True,null=True)
    sec_school_board=models.CharField(max_length=50,null=True,blank=True)    
    sec_school_year=models.CharField(max_length=50,null=True,blank=True)
    sec_school_details=models.CharField(max_length=500,null=True,blank=True)
    higher_sec_school=models.CharField(max_length=50,blank=True,null=True)
    perc_in_higher_sec_school=models.CharField(max_length=100,blank=True,null=True)
    higher_sec_school_board=models.CharField(max_length=50,null=True,blank=True)    
    higher_sec_year=models.CharField(max_length=50,null=True,blank=True)
    higher_sec_school_details=models.CharField(max_length=500,null=True,blank=True)
    college=models.CharField(max_length=50,blank=True,null=True)
    degree=models.CharField(max_length=100,null=True,blank=True)
    college_year=models.CharField(max_length=100,null=True,blank=True)
    university=models.CharField(max_length=100,null=True,blank=True)
    college_details=models.CharField(max_length=500,null=True,blank=True)
    perc_in_college=models.CharField(max_length=100,blank=True,null=True)
    experience=models.CharField(max_length=50,null=True,blank=True)
    resume =models.FileField(upload_to='resume')
    phone=models.CharField(max_length=15)
    email=models.EmailField(max_length=50,blank=True,null=True)
    current_address=models.TextField(max_length=100,blank=True, null=True)
    permanent_address=models.TextField(max_length=300,null=True,blank=True)
    
    
class Skills(models.Model):
   skill=models.CharField(max_length=250,null=True,blank=True)
   
   def __str__(self):
       return self.skill
    
class WorkExp(models.Model):
    comapny_name=models.CharField(max_length=100,null=True,blank=True)
    join_date=models.DateField(null=True,blank=True)
    end_date=models.DateField(null=True, blank=True)
    project_title=models.CharField(max_length=100)
    project_details=RichTextField(null=True, blank=True)
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
    
        
