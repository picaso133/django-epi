# Generated by Django 2.2.9 on 2020-01-14 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checks', '0008_auto_20200114_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
