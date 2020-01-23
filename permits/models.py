from django.db import models
from file_storage.models import Files_storage
from projects.models import Project

class Permit(models.Model):
    # Fields
    number = models.CharField(max_length=255)
    types = [
        ('Electric', 'Electric'),
        ('Plumbing', 'Plumbing'),
        ('Building', 'Building'),
        ('Parking', 'Parking'),
    ]
    type = models.CharField(max_length=255, choices=types)
    description = models.TextField(blank=True)
    start_date = models.DateField(blank=True, default='1970-01-01')
    end_date = models.DateField(blank=True, default='1970-01-01')

    # Relations
    file = models.ForeignKey(Files_storage, models.SET_NULL, blank=True, null=True)
    project = models.ForeignKey(Project, models.SET_NULL, blank=True, null=True, related_name='permits')

    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Permit'
        verbose_name_plural = 'Permits'

    def __str__(self):
        return self.type + self.number
