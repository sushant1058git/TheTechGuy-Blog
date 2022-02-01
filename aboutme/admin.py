from django.contrib import admin
from .models import *
from import_export.admin import ImportExportMixin




class ContactAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('email', 'name', 'subject')
    list_display_links = ('email',)


admin.site.register(AboutMe)
admin.site.register(Skills)
admin.site.register(WorkExp)
admin.site.register(PersonalProjects)
admin.site.register(SocialLinks)
admin.site.register(Contact, ContactAdmin)