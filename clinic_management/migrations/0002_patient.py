# Generated by Django 5.0.6 on 2024-06-02 16:07

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('birth_year', models.IntegerField()),
                ('phone', models.CharField(max_length=100)),
                ('note', models.TextField()),
                ('histories', models.TextField()),
                ('allergies', models.TextField()),
                ('medications', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]