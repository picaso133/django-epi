from django.db import models
from file_storage.models import Files_storage
from employees.models import Employ
from projects.models import Project
from suppliers.models import Supplier

class Customer(models.Model):
    # Fields
    name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)

    # Relations
    project = models.ForeignKey(Project, models.SET_NULL, blank=True, null=True)
    employ = models.ForeignKey(Employ, models.SET_NULL, blank=True, null=True)
    supplier = models.ForeignKey(Supplier, models.SET_NULL, blank=True, null=True)


    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
