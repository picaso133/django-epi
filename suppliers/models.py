from django.db import models
from projects.models import Project
from file_storage.models import Files_storage

class Supplier(models.Model):
    # Fields
    name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=255)
    contact_email = models.CharField(max_length=255)

    # Relations

    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)