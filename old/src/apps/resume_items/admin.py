from django.contrib import admin

from .models import ResumeLanguage, Education, WorkExperience


admin.site.register(ResumeLanguage)
admin.site.register(Education)
admin.site.register(WorkExperience)