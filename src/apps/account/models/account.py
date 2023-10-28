from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.common.models import BaseModel, RoleChoice
from src.apps.account.managers.account import UserManager


class User(AbstractUser, BaseModel):

    email = models.EmailField(
        'Email field',
        max_length=255,
        unique=True,
        db_index=True
    )
    avatar=models.ImageField(
        'Аватар',
        blank=True,
        null=True,
        upload_to='user/avatar'
    )
    first_name = models.CharField(
        'First name',
        max_length=100,
        null=True,
        blank=True
    )
    lastname = models.CharField(
        'Last name',
        max_length=100,
        null=True,
        blank=True
    )
    role = models.CharField('Role of a user', max_length=20, choices=RoleChoice.choices, 
                            default=RoleChoice.USER)
    is_active = models.BooleanField(
        'Active status',
        default=True
    )
    is_admin=models.BooleanField(
        'Superuser status',
        default=False
    )

    def get_full_name(self):
        return self.email

    def is_staff(self):
        return self.is_admin

    def get_shot_name(self):
        return self.email

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'