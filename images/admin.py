from django.contrib import admin
from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'filename', 'folder', 'thumbnail_uri', 'file')
    list_filter = ()
    search_fields = ('file',)

