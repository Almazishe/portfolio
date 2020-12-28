from slugify import slugify

from django.db import models

from utils.models import BaseModel


class University(BaseModel, models.Model):
    """ University model for resume """

    name = models.CharField(verbose_name='University name',
                            max_length=255)

    slug = models.SlugField(verbose_name='Slug',
                            unique=True,
                            blank=True)

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'
        ordering = ('slug',)

    def __str__(self) -> str:
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(University, self).save(*args, **kwargs)


class Faculty(BaseModel, models.Model):
    """ Faculty model. Faculty of the unoversity """

    university = models.ForeignKey(to=University,
                                   verbose_name='University',
                                   related_name='faculties',
                                   on_delete=models.CASCADE)

    name = models.CharField(verbose_name='Faculty',
                            max_length=255)

    slug = models.SlugField(verbose_name='Slug',
                            blank=True)

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'
        ordering = ('slug',)
        unique_together = ('university', 'slug')

    def __str__(self) -> str:
        return f'{self.university.name} | {self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Faculty, self).save(*args, **kwargs)
