from django.contrib import admin

from .models import Team, TeamComment


admin.site.register(Team)
admin.site.register(TeamComment)