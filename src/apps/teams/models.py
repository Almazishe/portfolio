from slugify import slugify

from django.db import models
from django.db.models import Sum
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

from utils.models import BaseModel, DateModel

# User auth model
User = get_user_model()


class Team(BaseModel, DateModel, models.Model):
    """ Team model """

    name = models.CharField(verbose_name='Team name',
                            default='Some happy team ♥',
                            max_length=255)

    slug = models.SlugField(verbose_name='Slug',
                            blank=True,
                            unique=True)

    creator = models.ForeignKey(to=User,
                                verbose_name='Team creator/owner',
                                on_delete=models.SET_NULL,
                                related_name='teams_owned',
                                null=True)

    stars = models.FloatField(verbose_name='Star rating',
                              default=0,
                              validators=(MinValueValidator(0),
                                          MaxValueValidator(10),),)

    description = models.TextField(verbose_name='Team description',
                                   null=True,
                                   blank=True)
    
    users = models.ManyToManyField(to=User,
                                   verbose_name='Teammates',
                                   blank=True,
                                   related_name='teams')

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'{self.name} | {self.creator.full_name}'

    def save(self, *args, **kwargs):
        if self.name == 'Some happy team ♥':
            self.slug = f'{slugify(self.name)}-{str(self.uuid)}'
        else:
            self.slug = slugify(self.name)
        super(Team, self).save(*args, **kwargs)

    def update_rating(self):
        rating_sum = self.comments.all().aggregate(Sum('rating'))['rating__sum']
        rating_count = self.comments.all().count()
        self.stars = (rating_sum * 1.0) / (rating_count * 1.0)
        self.save()


class TeamComment(BaseModel, DateModel, models.Model):
    """ Comment of user written to Team """

    team = models.ForeignKey(to=Team,
                             verbose_name='Team',
                             related_name='comments',
                             on_delete=models.CASCADE)
    user = models.ForeignKey(to=User,
                             verbose_name='User',
                             related_name='written_comments',
                             on_delete=models.CASCADE,)
    rating = models.FloatField(verbose_name='Rating given',
                               validators=(MinValueValidator(0),
                                           MaxValueValidator(10),)
                               )
    comment = models.TextField(verbose_name='Comment text',
                               null=True,
                               blank=True)

    class Meta:
        verbose_name = 'Team comment'
        verbose_name_plural = 'Team comments'
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'{self.user.full_name} ♥ {self.team.name} = {self.rating}'

    def save(self, *args, **kwargs):
        self.team.update_rating()
        super(TeamComment, self).save(*args, **kwargs)
