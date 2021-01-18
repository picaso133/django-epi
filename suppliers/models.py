from django.db import models
from projects.models import Project
from file_storage.models import Files_storage

class Supplier(models.Model):
    # Fields
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, default='')
    contact_name = models.CharField(max_length=255, blank=True, default='')
    contact_phone = models.CharField(max_length=255, blank=True, default='')
    contact_email = models.CharField(max_length=255, blank=True, default='')

    # Relations

    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name + " [" + self.address + ']'