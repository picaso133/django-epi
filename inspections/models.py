from django.db import models
from projects.models import Project
from inspection_types.models import Inspection_type

class Inspection(models.Model):
    date = models.DateTimeField()
    description = models.TextField(blank=True)
    status = [
        ('Passed', 'Passed'),
        ('Failed', 'Failed'),
        ('Partial', 'Partial'),
        ('Scheduled', 'Scheduled'),
    ]
    status = models.CharField(
        max_length=255,
        choices=status,
        default = 'Scheduled'
    )
    confirmation_number = models.IntegerField(blank=True)

    type = models.ForeignKey(Inspection_type, models.SET_NULL, blank=True, null=True)
    project = models.ForeignKey(Project, models.SET_NULL, blank=True, null=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Inspection'
        verbose_name_plural = 'Inspections'

    def __str__(self):
        return str(self.type) + ' ' + str(self.confirmation_number)

