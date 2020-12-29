import datetime

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from slugify import slugify

from apps.resume_items.languages.models import Language
from apps.resume_items.universities.models import University, Faculty
from apps.resumes.models import Resume
from utils.models import BaseModel, DateModel


def current_year():
    return datetime.date.today().year


class ResumeLanguage(BaseModel, DateModel, models.Model):
    """ Language that will be in resume with level """

    LAN_LEVELS = (
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C1', 'C1'),
        ('C2', 'C2'),
    )

    language = models.ForeignKey(to=Language,
                                 verbose_name='Language',
                                 on_delete=models.CASCADE)
    resume = models.ForeignKey(to=Resume,
                               verbose_name='Resume',
                               on_delete=models.CASCADE,
                               related_name='resume_languages')
    level = models.CharField(verbose_name='Level',
                             max_length=2,
                             choices=LAN_LEVELS,
                             default='A1')

    class Meta:
        verbose_name = 'ResumeLanguage'
        verbose_name_plural = 'ResumeLanguages'
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'{self.resume.owner.full_name} | {self.language.name} | {self.level}'


class Education(BaseModel, DateModel, models.Model):
    """ User resumes education """

    year_choices = [(r, r) for r in range(1984, datetime.date.today().year + 10)]

    resume = models.ForeignKey(to=Resume,
                               verbose_name='User resume',
                               on_delete=models.CASCADE,
                               related_name='resume_educations')

    university = models.ForeignKey(to=University,
                                   verbose_name='University',
                                   on_delete=models.SET_NULL,
                                   related_name='university_students',
                                   null=True)

    faculty = models.ForeignKey(to=Faculty,
                                verbose_name='Faculty',
                                blank=True,
                                null=True,
                                default=None,
                                on_delete=models.SET_NULL,
                                related_name='faculty_students')

    gpa = models.FloatField(verbose_name='GPA',
                            null=True,
                            blank=True,
                            default=0)

    start_year = models.PositiveIntegerField(verbose_name='Start year',
                                             choices=year_choices,
                                             default=current_year, )

    end_year = models.PositiveIntegerField(verbose_name='End year',
                                           choices=year_choices,
                                           default=current_year, )

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Educations'
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'{self.resume.owner.full_name} | {self.university.name}'


class WorkExperience(BaseModel, DateModel, models.Model):
    """ Word experience model """

    company = models.CharField(verbose_name='Company / Project name',
                               max_length=255)

    role = models.TextField(verbose_name='Role in company / Or short description of project',
                            blank=True,
                            null=True)

    responsibilities = models.TextField(verbose_name='Responsibilities description / Or Full description of project',
                                        blank=True,
                                        null=True)

    start_date = models.DateField(verbose_name='Start date')

    end_date = models.DateField(verbose_name='End date',
                                blank=True,
                                null=True,
                                default=None,
                                help_text='Make null if "work till this moment"')

    resume = models.ForeignKey(Resume,
                               verbose_name='Resume users/teams',
                               on_delete=models.CASCADE,
                               related_name='work_experiences', )

    class Meta:
        verbose_name = 'Work experience'
        verbose_name_plural = 'Work experiences'
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'Work experience of {self.resume.owner.full_name}'
