from django.db import models
from projects.models import Project
from file_storage.models import Files_storage
from documents.models import Document
from invoices.models import Invoice

class Change_order(models.Model):
    # Fields
    status_type = [
        ('Open', 'Open'),
        ('Sent', 'Sent'),
        ('Under Review', 'Under Review'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Canceled', 'Canceled'),
    ]
    status = models.CharField(max_length=255, choices=status_type, default='Open')

    # Relations
    project = models.ForeignKey(Project, models.SET_NULL, blank=True, null=True)
    document = models.ForeignKey(Document, models.SET_NULL, blank=True, null=True)
    invoice = models.ForeignKey(Invoice, models.SET_NULL, blank=True, null=True)

    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.document.number) + self.project