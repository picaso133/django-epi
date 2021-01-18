import uuid
from django.db import models
from file_storage.models import Files_storage
from employees.models import Employ


# https://www.beginner-bookkeeping.com/accounting-source-documents.html
class Document_type(models.Model):
    # Fields
    name = models.CharField(max_length=255)
    prefix = models.CharField(max_length=255, blank=True, default='')
    postfix = models.CharField(max_length=255, blank=True, default='')
    start = models.PositiveIntegerField(default=0)

    # Auto generated fields
    uuid = models.UUIDField(default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Document(models.Model):
    # Fields
    number = models.CharField(max_length=255, blank=True)
    date = models.DateTimeField(blank=True)
    description = models.TextField(blank=True)
    amount = models.FloatField(blank=True, default=0)
    # https://support.taulia.com/articles/en_US/Agent_Knowledge_Base/Q-What-are-the-different-invoice-statuses-1449537733733
    statuses = [
        ('Approved', 'Approved'),
        ('Cleared', 'Cleared '),
        ('Draft ', 'Draft '),
        ('In Process', 'In Process'),
        ('Paid ', 'Paid '),
        ('Pending Cancellation', 'Pending Cancellation'),
        ('Pending Review', 'Pending Review'),
        ('Rejected', 'Rejected'),
        ('Submitting ', 'Submitting '),
        ('Unpaid ', 'Unpaid '),
    ]
    status = models.CharField(max_length=255, choices=statuses, default='Pending Review')

    # Relations
    type = models.ForeignKey(Document_type, models.SET_NULL, blank=True, null=True)
    files = models.ManyToManyField(Files_storage)

    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def get_number(self):
        return self.type.prefix + self.number + self.type.postfix

    def __str__(self):
        return self.get_number()
