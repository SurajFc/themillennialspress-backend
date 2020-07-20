# Generated by Django 3.0.8 on 2020-07-12 05:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=250, primary_key=True, serialize=False, verbose_name='User ID'),
        ),
    ]
