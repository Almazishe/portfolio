from django.db import models
from slugify import slugify

from utils.models import BaseModel, DateModel


class Stack(BaseModel, DateModel, models.Model):
    """ User stack Python, Java, C#, JS... """

    name = models.CharField(verbose_name='Stack',
                            max_length=255,)
    slug = models.SlugField(verbose_name='Slug',
                            unique=True,
                            blank=True)

    class Meta:
        verbose_name = 'Stack'
        verbose_name_plural = 'Stacks'
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Stack, self).save(*args, **kwargs)
