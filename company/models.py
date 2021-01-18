from django.db import models
from file_storage.models import Files_storage

class Company(models.Model):
    # Fields
    name = models.CharField(max_length=255, blank=True)
    address = models.DateTimeField(blank=True)
    license = models.CharField(max_length=255, blank=True)
    # Relations
    files = models.ManyToManyField(Files_storage)

    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.number + ' [' + self.payee + '] - ' + str(self.amount)
