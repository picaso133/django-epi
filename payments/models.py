from django.db import models
from customers.models import Customer
from documents.models import Document

class Payment(models.Model):
    # Fields

    # Relations
    document = models.ForeignKey(Document, models.SET_NULL, blank=True, null=True)
    customer = models.ForeignKey(Customer, models.SET_NULL, blank=True, null=True)

    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
