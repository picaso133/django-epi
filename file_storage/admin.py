from django.contrib import admin
from .models import Files_storage


class view(admin.ModelAdmin):
    list_display = ('file_name','file', 'file_size', 'uuid')
    search_fields = ['file', 'uuid']

admin.site.register(Files_storage, view)