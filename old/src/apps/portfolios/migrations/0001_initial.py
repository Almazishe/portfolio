# Generated by Django 3.1.4 on 2020-12-31 05:21

import apps.portfolios.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0003_team_logo'),
        ('stacks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at date')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, verbose_name='Slug')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('img_1', models.ImageField(upload_to=apps.portfolios.models.get_img_path, verbose_name='Image #1')),
                ('img_2', models.ImageField(upload_to=apps.portfolios.models.get_img_path, verbose_name='Image #2')),
                ('img_3', models.ImageField(upload_to=apps.portfolios.models.get_img_path, verbose_name='Image #3')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link to project')),
                ('git_link', models.URLField(blank=True, null=True, verbose_name='Github link')),
                ('stack', models.ManyToManyField(related_name='projects', to='stacks.Stack')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at date')),
                ('is_team_porfolio', models.BooleanField(default=False, verbose_name='Is Team porfolio?')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='portfolios', to=settings.AUTH_USER_MODEL, verbose_name='Owner User')),
                ('team', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='portfolios', to='teams.team', verbose_name='Team')),
            ],
            options={
                'ordering': ('-uuid',),
                'abstract': False,
            },
        ),
    ]