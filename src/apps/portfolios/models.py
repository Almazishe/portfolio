from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify

from apps.resume_items.stacks.models import Stack
from apps.teams.models import Team

from utils.views import get_path
from utils.models import BaseModel, DateModel

# User auth model
User = get_user_model()


def get_img_path(instance, filename):
    return get_path(instance, filename, 'projects_images')


class Project(BaseModel, DateModel, models.Model):
    """ Portfolio project model """

    title = models.CharField(verbose_name='Title',
                             max_length=255)
    slug = models.SlugField(verbose_name='Slug',
                            blank=True)
    description = models.TextField(verbose_name='Description',
                                   null=True,
                                   blank=True)

    img_1 = models.ImageField(verbose_name="Image #1",
                              upload_to=get_img_path)
    img_2 = models.ImageField(verbose_name="Image #2",
                              upload_to=get_img_path)
    img_3 = models.ImageField(verbose_name="Image #3",
                              upload_to=get_img_path)
    
    link = models.URLField(verbose_name='Link to project',
                           null=True,
                           blank=True)
    git_link = models.URLField(verbose_name='Github link',
                               null=True,
                               blank=True)
    stack = models.ManyToManyField(to=Stack,
                                   related_name='projects',)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ('-created_at',)

    def __str__(self) -> str:
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)


class Portfolio(BaseModel, DateModel, models.Model):
    """ Portfolio model """

    owner = models.ForeignKey(to=User,
                              related_name='portfolios',
                              on_delete=models.SET_NULL,
                              verbose_name='Owner User',
                              null=True)
    team = models.ForeignKey(to=Team,
                             related_name='portfolios',
                             verbose_name='Team',
                             on_delete=models.SET_NULL,
                             null=True)
    is_team_porfolio = models.BooleanField(verbose_name='Is Team porfolio?',
                                           default=False)

