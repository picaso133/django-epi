from django.db import models
import uuid

class Inspection_type(models.Model):
    category = [
        ('Electrical', 'Electrical'),
        ('Plumbing', 'Plumbing'),
        ('Building', 'Building'),
    ]
    category = models.CharField(
        max_length=255,
        choices=category
    )
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Inspection Type'
        verbose_name_plural = 'Inspection Types'

    def __str__(self):
        return '[' + self.category + '] ' + self.name