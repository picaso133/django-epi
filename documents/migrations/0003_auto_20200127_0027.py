# Generated by Django 2.2.9 on 2020-01-27 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0002_document_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='number',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
