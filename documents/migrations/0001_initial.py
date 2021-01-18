# Generated by Django 2.2.9 on 2020-01-27 08:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('file_storage', '0003_files_storage_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.TextField(blank=True)),
                ('date', models.DateTimeField(blank=True)),
                ('due_date', models.DateTimeField(blank=True)),
                ('payee', models.CharField(blank=True, max_length=255)),
                ('payer', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('amount', models.FloatField(blank=True, default=0)),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Cleared', 'Cleared '), ('Draft ', 'Draft '), ('In Process', 'In Process'), ('Paid ', 'Paid '), ('Pending Cancellation', 'Pending Cancellation'), ('Pending Review', 'Pending Review'), ('Rejected', 'Rejected'), ('Submitting ', 'Submitting '), ('Unpaid ', 'Unpaid ')], default='Pending Review', max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('files', models.ManyToManyField(to='file_storage.Files_storage')),
            ],
        ),
    ]