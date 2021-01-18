# Generated by Django 2.2.9 on 2020-01-28 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('file_storage', '0003_files_storage_description'),
        ('projects', '0023_auto_20200127_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='proposal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proposals', to='file_storage.Files_storage'),
        ),
    ]