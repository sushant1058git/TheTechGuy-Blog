from django.contrib import admin
from .models import Catagory, Blog, Tag, EmailSignUp,\
     Contact, Comment, Reply
from .models import *
from .forms import *

class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm

class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Catagory,CatAdmin)
admin.site.register(Blog,BlogAdmin)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Tag)
admin.site.register(EmailSignUp)
admin.site.register(Contact)

