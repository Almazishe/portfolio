from django.db import models
from django.contrib.auth import get_user_model

from apps.resume_items.stacks.models import Stack
from utils.models import BaseModel, DateModel

from apps.locations.models import City

# User account auth model
User = get_user_model()


class Resume(DateModel, BaseModel, models.Model):
    """ Users/Teams Base resume model """

    owner = models.ForeignKey(to=User,
                              verbose_name='Owner of resume',
                              on_delete=models.CASCADE, )
    link = models.URLField(verbose_name='Link to website or portfolio.',
                           blank=True,
                           null=True,
                           default=None,
                           help_text='If no website link here will be link to portfolio')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(verbose_name='Phone number',
                             max_length=15)
    main_city = models.ForeignKey(to=City,
                                  on_delete=models.SET_NULL,
                                  verbose_name='Search city',
                                  related_name='user_resumes',
                                  null=True)
    cities = models.ManyToManyField(to=City,
                                    verbose_name='Cities')
    stack = models.ManyToManyField(to=Stack,
                                   related_name='resumes')

    is_active = models.BooleanField(verbose_name='Active?',
                                    default=True)

    class Meta:
        abstract = True
        ordering = ('owner',)


class UserResume(Resume, models.Model):
    """ Users resume model """

    work_schedule = (
        ('full_time', 'Full time'),
        ('part_time', 'Part time'),
        ('shift', 'Shift method'),
        ('remote', 'Remote'),
    )

    vacancy = models.CharField(verbose_name='Vacancy',
                               max_length=255)

    work_method = models.CharField(verbose_name='Work schedule',
                                   max_length=20,
                                   choices=work_schedule,
                                   blank=True,
                                   null=True)

    class Meta:
        verbose_name = 'User resume'
        verbose_name_plural = 'User resumes'
        ordering = ('created_at',)

    def __str__(self) -> str:
        return f'Resume of {self.owner.full_name} user'
