# Generated by Django 2.2.9 on 2020-01-15 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20200115_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='permits',
        ),
        migrations.DeleteModel(
            name='Inspection',
        ),
        migrations.DeleteModel(
            name='Inspection_type',
        ),
    ]
