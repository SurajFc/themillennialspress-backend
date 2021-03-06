# Generated by Django 3.0.8 on 2020-07-23 05:19

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import image_optimizer.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', image_optimizer.fields.OptimizedImageField(upload_to='Articles/images/')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('added_by', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'ArticleImage',
                'verbose_name_plural': 'ArticleImages',
                'db_table': 'articleimage',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('image', image_optimizer.fields.OptimizedImageField(default='def.png', upload_to='category')),
                ('slug', models.SlugField(default=' ', unique=True)),
                ('description', models.TextField(blank=True, default=' ')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'category',
                'ordering': ('-updated_at',),
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, unique=True)),
                ('subtitle', models.CharField(blank=True, default=' ', max_length=255)),
                ('cover', image_optimizer.fields.OptimizedImageField(blank=True, upload_to='Articles')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=250), blank=True, size=None)),
                ('content', models.TextField()),
                ('author_name', models.CharField(max_length=240)),
                ('user', models.CharField(max_length=250)),
                ('realease', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.SlugField(default=' ', max_length=255, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Category', verbose_name='category_id')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'db_table': 'articles',
                'ordering': ('-updated_at',),
            },
        ),
    ]
