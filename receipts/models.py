import uuid
from django.db import models
from file_storage.models import Files_storage
from employees.models import Employ
from documents.models import Document
from customers.models import Customer
from suppliers.models import Supplier

class Receipt(models.Model):
    # Fields

    # Relations
    document = models.ForeignKey(Document, models.SET_NULL, blank=True, null=True)
    r_from = models.ForeignKey(Supplier, models.SET_NULL, blank=True, null=True)
    r_to = models.ForeignKey(Customer, models.SET_NULL, blank=True, null=True)
    files = models.ManyToManyField(Files_storage)

    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.document.get_number
