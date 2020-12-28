# Generated by Django 3.1.4 on 2020-12-27 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0004_auto_20201223_0816'),
        ('stacks', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResume',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at date')),
                ('link', models.URLField(blank=True, default=None, help_text='If no website link here will be link to portfolio', null=True, verbose_name='Link to website or portfolio.')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone number')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active?')),
                ('vacancy', models.CharField(max_length=255, verbose_name='Vacancy')),
                ('work_method', models.CharField(blank=True, choices=[('full_time', 'Full time'), ('part_time', 'Part time'), ('shift', 'Shift method'), ('remote', 'Remote')], max_length=20, null=True, verbose_name='Work schedule')),
                ('cities', models.ManyToManyField(to='locations.City', verbose_name='Cities')),
                ('main_city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_resumes', to='locations.city', verbose_name='Search city')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner of resume')),
                ('stack', models.ManyToManyField(related_name='resumes', to='stacks.Stack')),
            ],
            options={
                'verbose_name': 'User resume',
                'verbose_name_plural': 'User resumes',
                'ordering': ('created_at',),
            },
        ),
    ]
