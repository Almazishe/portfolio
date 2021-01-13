from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from utils.models import BaseDateModel


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Please, give us your email.')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            **extra_fields
        )

        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff=True required for Superuser')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser=True required for Superuser')

        user.save(using=self._db)
        return user


class Account(BaseDateModel, AbstractBaseUser, PermissionsMixin):
    ''' User Account Auth model '''

    MALE = 'MALE'
    FEMALE = 'FEMALE'
    SEX_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Male'),
    )

    email = models.EmailField(verbose_name='E-mail', max_length=64, unique=True,)
    is_email_verified = models.BooleanField(verbose_name='Verified email?', default=False,)
    first_name = models.CharField(verbose_name='First name', max_length=64, default='User',)
    last_name = models.CharField(verbose_name='Last name', max_length=64, default='Happy',)
    img = models.ImageField(verbose_name='User image', upload_to='accounts/images/', null=True, blank=True)
    birth_at = models.DateField(verbose_name='Birthday', null=True)
    sex = models.CharField(verbose_name='Sex', max_length=10, choices=SEX_CHOICES, default=MALE)
    is_staff = models.BooleanField(default=False, verbose_name='Staff?',)
    is_active = models.BooleanField(default=True, verbose_name='Active?',)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AccountManager()

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name} | {self.email}'

    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'

    @property
    def full_name(self):
        return self.get_full_name()
