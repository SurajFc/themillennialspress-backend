# Generated by Django 3.0.8 on 2020-07-15 11:05

from django.db import migrations, models
import image_optimizer.fields


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0008_articleimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleimages',
            name='image',
            field=image_optimizer.fields.OptimizedImageField(upload_to='Articles/images/'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]
