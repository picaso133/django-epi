import uuid
import mimetypes
from django.db import models

class Files_storage(models.Model):
    file = models.FileField(upload_to='uploads/', blank=True)
    description = models.CharField(max_length=255, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def file_name(self):
        return self.file.name.split('/')[1]

    def file_type(self):
        return str(mimetypes.guess_type(self.file.name)[0])

    def file_size(self):
        # return str(self.file.size / 1024 / 1024)[:5] + " MB"
        return str(round(self.file.size / 1024, 1)) + " KB"

    def file_path(self):
        return self.file.path

    def file_url(self):
        return '../uploads/' + self.file.name

    class Meta:
        verbose_name = 'File Storage'
        verbose_name_plural = 'File Storage'

    def __str__(self):
        return self.file.name