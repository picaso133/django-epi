from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from file_storage.models import Files_storage


class Employ(models.Model):
    name = models.CharField(max_length=255)
    address =  models.CharField(max_length=255, blank=True)
    phone =  models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    documents = models.ManyToManyField(Files_storage)
    user = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    # def get_absolute_url(self):
        # return reverse('employ', kwargs = {'slug': self.id_document.name})

    def __str__(self):
        return self.name