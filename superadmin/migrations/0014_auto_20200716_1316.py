# Generated by Django 3.0.8 on 2020-07-16 07:46

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0013_auto_20200716_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50), blank=True, size=None),
        ),
    ]
