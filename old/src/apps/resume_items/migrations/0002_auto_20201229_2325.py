# Generated by Django 3.1.4 on 2020-12-29 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resumes', '0001_initial'),
        ('resume_items', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ('-created_at',), 'verbose_name': 'Education', 'verbose_name_plural': 'Educations'},
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='resume_type',
        ),
        migrations.AddField(
            model_name='workexperience',
            name='resume',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='work_experiences', to='resumes.resume', verbose_name='Resume users/teams'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='education',
            name='resume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_educations', to='resumes.resume', verbose_name='User resume'),
        ),
    ]
