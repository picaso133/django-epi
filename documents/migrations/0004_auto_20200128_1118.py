# Generated by Django 2.2.9 on 2020-01-28 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_auto_20200127_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='payee',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='payer',
            field=models.TextField(blank=True),
        ),
    ]
