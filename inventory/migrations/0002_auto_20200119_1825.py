# Generated by Django 2.2.9 on 2020-01-20 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='project',
            new_name='category',
        ),
    ]
