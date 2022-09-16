from django.contrib import admin
from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from . import models


# Пост на сайте
class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = models.Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

    prepopulated_fields = {"slug": ("title",)}


admin.site.register(models.Post, PostAdmin)
