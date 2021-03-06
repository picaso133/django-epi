# Generated by Django 3.0.2 on 2020-01-04 21:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20200104_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inspection_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('EL', 'Electric'), ('PL', 'Plumbing'), ('BU', 'Building')], max_length=2)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Inspection Type',
                'verbose_name_plural': 'Inspection Types',
            },
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('confirmation_number', models.IntegerField(blank=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projects.Inspection_type', verbose_name='Inspection Type')),
            ],
            options={
                'verbose_name': 'Inspection',
                'verbose_name_plural': 'Inspections',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='inspections',
            field=models.ManyToManyField(to='projects.Inspection'),
        ),
    ]
