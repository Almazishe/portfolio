from django.db import models
from django.contrib.auth import get_user_model

from utils.models import BaseModel, DateModel

# User account auth model
User = get_user_model()


class Portfolio(DateModel, BaseModel, models.Model):
    """ Users portfolio model """

    user = models.ForeignKey(
        verbose_name='User',
        on_delete=models.CASCADE
    )

    vacancy = models.CharField(
        verbose_name='Vacancy',
        max_length=255,
    )

    salary = models.IntegerField(
        verbose_name='Ожидаемая зарплата',
        default=0,
    )
