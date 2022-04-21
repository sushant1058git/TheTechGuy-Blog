from django.contrib import admin
from .models import Catagory, Blog, Tag, EmailSignUp,\
     Contact, Comment, Reply
from .models import *
from import_export.admin import ImportExportMixin



class CatAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
    
class UserEmailAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('email',)
    # list_display_links = ('email',)s

admin.site.register(Catagory,CatAdmin)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(Tag)
admin.site.register(EmailSignUp,UserEmailAdmin)
admin.site.register(Contact)

