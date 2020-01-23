import uuid
from datetime import datetime
from django.utils.html import format_html
from django.db import models
from django.contrib.auth.models import User

from django_epi.settings import BASE_DIR
from file_storage.models import Files_storage
from resident_managers.models import Resident_manager
from project_managers.models import Project_manager
# from inspections.models import Inspection

class Design_package(models.Model):
    type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Design Package'
        verbose_name_plural = 'Design Packages'

    def __str__(self):
        return self.type

class General_contractor(models.Model):
    company = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    email = models.EmailField()
    order_email = models.EmailField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def full_name(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = 'General Contractor'
        verbose_name_plural = 'General Contractors'

    def __str__(self):
        return self.first_name + " " + self.last_name

class Project(models.Model):
    # Fields
    legal_entity = models.CharField(max_length=255, blank=True)
    portfolio = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255)
    unit = models.IntegerField(blank=True, default=0)
    zip = models.IntegerField(blank=True, default=0)
    city_state = models.CharField(max_length=255, default="")
    passwords = models.CharField(max_length=255, blank=True)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    sqFt = models.FloatField()
    percent = models.FloatField(default=0)
    jobNumber = models.CharField(max_length=255, unique=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    status_type = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Under Review', 'Under Review'),
        ('Approved', 'Approved'),
        ('Done', 'Done'),
        ('Canceled', 'Canceled'),
        ('Rejected', 'Rejected')
    ]
    status = models.CharField(max_length=255, choices=status_type, default='OPEN')

    # Relations
    pm_epi = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, verbose_name = "Project Manager EPI")
    rm = models.ForeignKey(Resident_manager, models.SET_NULL, blank=True, null=True, verbose_name = "Resident Manager")
    pm = models.ForeignKey(Project_manager, models.SET_NULL, blank=True, null=True, verbose_name = "Project Manager")
    general_contractor = models.ForeignKey(General_contractor, models.SET_NULL, blank=True, null=True, verbose_name = "General Contractor")
    design_package = models.ForeignKey(Design_package, models.SET_NULL, blank=True, null=True, verbose_name = "Design package")
    drawings = models.ManyToManyField(Files_storage)

    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.address + ' #' + str(self.unit)
