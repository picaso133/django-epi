from django.db import models
from projects.models import Project
from file_storage.models import Files_storage
from suppliers.models import Supplier

class Order(models.Model):
    # Fields
    number = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    status_type = [
        ('Pending', 'Pending'),
        ('Awaiting Payment', 'Awaiting Payment'),
        ('Awaiting Fulfillment', 'Awaiting Fulfillment'),
        ('Awaiting Shipment', 'Awaiting Shipment'),
        ('Awaiting Pickup', 'Awaiting Pickup'),
        ('Partially Shipped', 'Partially Shipped'),
        ('Completed', 'Completed'),
        ('Shipped', 'Shipped'),
        ('Canceled', 'Canceled'),
        ('Declined', 'Declined'),
        ('Refunded', 'Refunded'),
        ('Disputed', 'Disputed'),
        ('Manual Verification Required', 'Manual Verification Required'),
        ('Partially Refunded', 'Partially Refunded')
    ]
    status = models.CharField(max_length=255, choices=status_type, default='Pending')

    # Relations
    project = models.ForeignKey(Project, models.SET_NULL, blank=True, null=True, related_name='orders')
    supplier = models.ForeignKey(Supplier, models.SET_NULL, blank=True, null=True, related_name='orders')
    files = models.ManyToManyField(Files_storage)

    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.number)

