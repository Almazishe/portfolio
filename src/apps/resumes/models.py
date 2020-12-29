from django.db import models
from django.contrib.auth import get_user_model

from utils.models import BaseModel, DateModel

from apps.teams.models import Team
from apps.locations.models import City
from apps.resume_items.stacks.models import Stack

# User auth model
User = get_user_model()


class Resume(DateModel, BaseModel, models.Model):
    """ Users/Teams Base resume model """
    work_schedule = (
        ('full_time', 'Full time'),
        ('part_time', 'Part time'),
        ('shift', 'Shift method'),
        ('remote', 'Remote'),
    )

    owner = models.ForeignKey(User,
                              verbose_name='Resume owner user',
                              on_delete=models.CASCADE,
                              related_name='resumes', )

    teams = models.ManyToManyField(Team,
                                   verbose_name='Resume owner team',
                                   related_name='resumes')

    vacancy = models.CharField(verbose_name='Vacancy',
                               max_length=255)

    work_method = models.CharField(verbose_name='Work schedule',
                                   max_length=20,
                                   choices=work_schedule,
                                   blank=True,
                                   null=True)

    link = models.URLField(verbose_name='Link to website or portfolio.',
                           blank=True,
                           null=True,
                           help_text='If no website link here will be link to portfolio')
    git_link = models.URLField(verbose_name='GitHub link',
                               blank=True,
                               null=True, )
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(verbose_name='Phone number',
                             max_length=15)

    main_city = models.ForeignKey(to=City,
                                  on_delete=models.SET_NULL,
                                  verbose_name='Search city',
                                  related_name='main_resumes',
                                  null=True)
    cities = models.ManyToManyField(to=City,
                                    verbose_name='resumes_in')
    stack = models.ManyToManyField(to=Stack,
                                   related_name='resumes')

    is_active = models.BooleanField(verbose_name='Active?',
                                    default=True)

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'{self.owner.full_name}s resume'
