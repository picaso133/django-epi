from django.db import models
from customers.models import Customer
from payments.models import Payment
from documents.models import Document


class Invoice(models.Model):
    # Fields
    due_date = models.DateField(blank=True, null=True)

    # Relations
    document = models.ForeignKey(Document, models.SET_NULL, blank=True, null=True)
    customer = models.ForeignKey(Customer, models.SET_NULL, blank=True, null=True)
    payments = models.ManyToManyField(Payment)

    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
