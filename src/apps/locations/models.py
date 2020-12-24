from django.db import models
from slugify import slugify


class Country(models.Model):
    """ Country's model """

    name = models.CharField(
        verbose_name='Country name',
        max_length=255,
    )

    slug = models.SlugField(
        unique=True,
        max_length=255,
        blank=True,
        editable=False
    )

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ('name',)

    def __str__(self) -> str:
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Country, self).save(*args, **kwargs)


class City(models.Model):
    """ City's model """

    country = models.ForeignKey(
        to=Country,
        on_delete=models.CASCADE,
        verbose_name='Country',
        related_name='cities'
    )

    name = models.CharField(
        verbose_name='City name',
        max_length=255
    )

    slug = models.SlugField(
        unique=True,
        max_length=255,
        blank=True,
        editable=False,
    )

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self) -> str:
        return f'{self.name}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super(City, self).save(*args, **kwargs)
