from django import forms
from .models import *

class BlogAdminForm(forms.ModelForm):
    detail = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))

    class Meta:
        model = Blog
        fields = "__all__"