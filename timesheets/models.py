from django.db import models
from datetime import datetime, timedelta
from projects.models import Project
from file_storage.models import Files_storage
from suppliers.models import Supplier
from employees.models import Employ

class Timesheet(models.Model):
    # Fields
    date = models.DateTimeField(blank=True)
    clock_in = models.TimeField(blank=True)
    clock_out = models.TimeField(blank=True)
    is_holiday = models.BooleanField(blank=True)
    is_meal_time = models.BooleanField(blank=True, default=False)
    is_weekend = models.BooleanField(blank=True)
    description = models.TextField(blank=True)

    # Relations
    project = models.ForeignKey(Project, models.SET_NULL, blank=True, null=True)
    employ = models.ForeignKey(Employ, models.SET_NULL, blank=True, null=True)

    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def hours(self):
        if self.is_meal_time:
            return datetime.strptime(str(self.clock_out), '%H:%M:%S') - datetime.strptime(str(self.clock_in), '%H:%M:%S') - timedelta(hours=1)
        else:
            return datetime.strptime(str(self.clock_out), '%H:%M:%S') - datetime.strptime(str(self.clock_in), '%H:%M:%S')

    # def __str__(self):
    #     return str(self.number)
