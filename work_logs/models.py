import uuid
from django.db import models
from projects.models import Project
from file_storage.models import Files_storage
from employees.models import Employ

class Work_log_types(models.Model):
    # Fields
    name = models.CharField(max_length=255, blank=True)
    short_name = models.CharField(max_length=255, blank=True)

    # Relations

    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return '[' + self.short_name + '] ' + self.name


class Work_log(models.Model):
    # Fields
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    statuses = [
        ('Holding', 'Holding'),
        ('Prioritized', 'Prioritized'),
        ('Started', 'Started'),
        ('Finished', 'Finished'),
    ]
    status = models.CharField(max_length=255, choices=statuses, default='Holding')

    # Relations
    project = models.ForeignKey(Project, models.SET_NULL, blank=True, null=True, related_name='Work_log')
    work_log_type = models.ForeignKey(Work_log_types, models.SET_NULL, blank=True, null=True)
    files = models.ManyToManyField(Files_storage)
    employees = models.ManyToManyField(Employ, related_name='employees_list')

    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.work_log_type.short_name + ' : ' + self.title
