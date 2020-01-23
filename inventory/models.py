from django.db import models
from file_storage.models import Files_storage

class Inventory_category(models.Model):
    # Fields
    name = models.CharField(max_length=255)

    # Relations

    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Inventory(models.Model):
    # Fields
    name = models.CharField(max_length=255)
    qty = models.IntegerField(blank=True)
    number = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    # Relations
    category = models.ForeignKey(Inventory_category, models.SET_NULL, blank=True, null=True)
    file = models.ForeignKey(Files_storage, models.SET_NULL, blank=True, null=True)

    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.number)

