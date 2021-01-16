from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from utils.models import BaseDateModel


User = get_user_model()


class TeamMember(BaseDateModel, models.Model):
    """
    Team member model  Users <-> Teams
    """
    LEVEL_ADMIN = "ADMIN_LEVEL_OF_TEAM_MEMBER"
    LEVEL_USER = "USER_LEVEL_OF_TEAM_MEMBER"
    LEVEL_CHOICES = (
        (LEVEL_ADMIN, _('Admin')),
        (LEVEL_USER, _('User')),
    )

    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE, related_name="related_teams")
    team = models.ForeignKey('Team', verbose_name=_("Team"), on_delete=models.CASCADE, related_name="related_users")
    level = models.CharField(_("Level"), max_length=100, choices=LEVEL_CHOICES, default=LEVEL_USER)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} | {self.team.name}'

class Team(BaseDateModel, models.Model):
    """
     Team model
    """

    owner = models.ForeignKey(User, verbose_name=_("Owner"), on_delete=models.SET_NULL, null=True, related_name='owned_teams')
    name = models.CharField(_("Name"), max_length=255)
    logo = models.ImageField(_("Logo"), null=True, blank=True, upload_to='teams/logos/')
    banner = models.ImageField(_("Banner"), null=True, blank=True, upload_to='teams/banners/')
    short_description = models.TextField(_("Short description"), null=True, blank=True)
    description = models.TextField(_("Description"), null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

