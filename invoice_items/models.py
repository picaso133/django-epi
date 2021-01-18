from django.db import models
from invoices.models import Invoice

class Invoice_item(models.Model):
    # Fields
    description = models.TextField(blank=True)
    unit_price = models.FloatField(blank=True, default=0)
    qty = models.FloatField(blank=True, default=1)
    amount = models.FloatField(blank=True, default=0)
    # Relations
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, blank=True, null=True, related_name='items')
    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)