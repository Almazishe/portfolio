# Generated by Django 3.1.4 on 2020-12-22 10:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at date')),
                ('email', models.EmailField(max_length=64, unique=True, verbose_name='E-mail')),
                ('is_email_verified', models.BooleanField(default=False, verbose_name='Verified email?')),
                ('first_name', models.CharField(default='User', max_length=64, verbose_name='First name')),
                ('last_name', models.CharField(default='Happy', max_length=64, verbose_name='Last name')),
                ('phone_number', models.CharField(max_length=15, unique=True, verbose_name='Phone number')),
                ('birth_at', models.DateField(verbose_name='Birthday')),
                ('sex', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Male'), ('OTHER', 'Other')], default='MALE', max_length=10, verbose_name='Sex')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active?')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
                'ordering': ('-created_at',),
            },
        ),
    ]
