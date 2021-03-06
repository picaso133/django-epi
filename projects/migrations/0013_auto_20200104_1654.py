# Generated by Django 2.2.9 on 2020-01-05 00:54

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('projects', '0012_auto_20200104_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='permits',
        ),
        migrations.AddField(
            model_name='project',
            name='permits',
            field=filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='project_permit', to=settings.FILER_IMAGE_MODEL),
        ),
    ]
