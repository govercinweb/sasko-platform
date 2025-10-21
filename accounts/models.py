from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _

from auditlog.registry import auditlog

from accounts.managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


auditlog.register(
    User,
    m2m_fields=['groups', 'user_permissions'],
    mask_fields=['password'],
    exclude_fields=['last_login'],
)
