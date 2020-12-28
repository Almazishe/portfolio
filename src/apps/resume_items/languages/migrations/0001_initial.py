# Generated by Django 3.1.4 on 2020-12-27 05:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at date')),
                ('name', models.CharField(max_length=255, verbose_name='Language')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
                'ordering': ('-created_at',),
            },
        ),
    ]
