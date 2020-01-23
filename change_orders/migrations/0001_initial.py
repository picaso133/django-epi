# Generated by Django 2.2.9 on 2020-01-19 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0018_auto_20200119_1350'),
        ('file_storage', '0003_files_storage_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Change_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True)),
                ('date', models.DateTimeField()),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Sent', 'Sent'), ('Under Review', 'Under Review'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Canceled', 'Canceled')], default='Open', max_length=255)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('files', models.ManyToManyField(to='file_storage.Files_storage')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='change_orders', to='projects.Project')),
            ],
            options={
                'verbose_name': 'Change Order',
                'verbose_name_plural': 'Change Orders',
            },
        ),
    ]
