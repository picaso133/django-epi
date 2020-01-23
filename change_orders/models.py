from django.db import models
from projects.models import Project
from file_storage.models import Files_storage

class Change_order(models.Model):
    # Fields
    number = models.IntegerField(blank=True)
    date = models.DateTimeField()
    description = models.TextField(blank=True)
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
    project = models.ForeignKey(Project, models.SET_NULL, blank=True, null=True, related_name='change_orders')
    files = models.ManyToManyField(Files_storage)

    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Change Order'
        verbose_name_plural = 'Change Orders'

    def __str__(self):
        return str(self.number)

