from django.db import models
import datetime
from documents.models import Document

class Check(models.Model):
    # Fields

    # Relations
    document = models.ForeignKey(Document, models.SET_NULL, blank=True, null=True)

    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.document.number) + self.document.payee