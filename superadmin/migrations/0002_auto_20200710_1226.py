# Generated by Django 3.0.8 on 2020-07-10 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
