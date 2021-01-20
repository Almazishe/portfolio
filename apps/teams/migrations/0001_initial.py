# Generated by Django 3.1.4 on 2021-01-13 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at date')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='teams/logos/', verbose_name='Logo')),
                ('banner', models.ImageField(blank=True, null=True, upload_to='teams/banners/', verbose_name='Banner')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='Short description')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owned_teams', to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at date')),
                ('level', models.CharField(choices=[('ADMIN_LEVEL_OF_TEAM_MEMBER', 'Admin'), ('USER_LEVEL_OF_TEAM_MEMBER', 'User')], default='USER_LEVEL_OF_TEAM_MEMBER', max_length=100, verbose_name='Level')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_users', to='teams.team', verbose_name='Team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_teams', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]