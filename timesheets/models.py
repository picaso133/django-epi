from django.db import models
from projects.models import Project
from file_storage.models import Files_storage
from suppliers.models import Supplier
from employees.models import Employ

class Timesheet(models.Model):
    # Fields
    date = models.DateTimeField()
    clock_in = models.TimeField()
    clock_out = models.TimeField()
    is_holiday = models.BooleanField()
    is_weekend = models.BooleanField()
    description = models.TextField(blank=True)

    # Relations
    project = models.ForeignKey(Project, models.SET_NULL, blank=True, null=True)
    employ = models.ForeignKey(Employ, models.SET_NULL, blank=True, null=True)

    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return str(self.number)

