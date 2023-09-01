from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'serial_number')
    list_filter = ('id', 'name', 'serial_number')
    search_fields = ('id', 'name', 'serial_number')

