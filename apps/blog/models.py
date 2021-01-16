from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.urls import reverse

from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase

from slugify import slugify

from utils.models import BaseDateModel
from apps.teams.models import Team


User = get_user_model()

class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

class Post(BaseDateModel, models.Model):
    """
    Post model for blog, User's or team's
    """

    owner = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE, related_name='created_posts', null=True)
    title = models.CharField(_("Title"), max_length=255, null=True)
    slug = models.SlugField(_("Slug"), max_length=255, unique=True, null=True, blank=True)
    image = models.ImageField(_("Image"), null=True, blank=True, upload_to='posts/images/')
    text = models.TextField(_("Text"), null=True, blank=True)
    is_team_post = models.BooleanField(_("Is Team Post"), default=False)
    team = models.ForeignKey(
        Team, verbose_name=_("Team"), on_delete=models.SET_NULL, related_name='related_posts', null=True, blank=True)

    tags = TaggableManager(through=UUIDTaggedItem)

    def __str__(self):
        if self.is_team_post:
            return f'{self.team.name} -> {self.title}'
        return f'{self.owner} -> {self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

class PostComment(BaseDateModel, models.Model):
    """
    Comment for Post
    """

    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE)
    text = models.TextField(_("Text"))
    parent = models.ForeignKey('self', verbose_name=_("Parent"), on_delete=models.SET_NULL, null=True, blank=True, related_name='children')
    post = models.ForeignKey(Post, verbose_name=_("Post"), on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f'{self.user} -> {self.post.title}:\n{self.text}'