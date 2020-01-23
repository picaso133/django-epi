from django.db import models

class Project_manager(models.Model):
    # Fields
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)

    # Relations


    # Auto generated fields
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Resident Manager'
        verbose_name_plural = 'Resident Managers'

    def __str__(self):
        return self.name
