from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class RoleChoice(models.TextChoices):
    ADMIN = "admin", _("admin")
    USER = "user", _("user")
    WAITER = "waiter", _("waiter")




