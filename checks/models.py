from django.db import models
import datetime

class Check(models.Model):
    number = models.IntegerField(unique=True)
    date = models.DateField(blank=True, null=True)
    pay_to = models.CharField(max_length=255, blank=True)
    pay_for = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    amount = models.FloatField(blank=True, default=0)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.number) + self.pay_to
