# Generated by Django 3.0.8 on 2020-07-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0016_auto_20200717_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='slug',
            field=models.SlugField(default=' '),
        ),
    ]
