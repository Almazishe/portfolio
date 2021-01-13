from django.db import models
from slugify import slugify

from utils.models import BaseModel, DateModel


class Language(BaseModel, DateModel, models.Model):
    """ Language model for resume A1, A2 ... """

    name = models.CharField(verbose_name='Language',
                            max_length=255)

    slug = models.SlugField(verbose_name='Slug',
                            unique=True,
                            blank=True)

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Language, self).save(*args, **kwargs)
