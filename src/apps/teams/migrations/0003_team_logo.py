# Generated by Django 3.1.4 on 2020-12-31 05:21

import apps.teams.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_team_stack'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=apps.teams.models.get_img_path, verbose_name='Team logo'),
        ),
    ]
