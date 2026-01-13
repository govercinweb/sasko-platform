from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.utils.translation import gettext as _

from auditlog.registry import auditlog

from accounts.managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    merchant = models.ForeignKey(
        'Merchant',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    roles = models.ManyToManyField('accounts.Role', blank=True)

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_role_permissions(self):
        return set(['{1}.{0}'.format(*p.natural_key()) for p in Permission.objects.filter(role__in=self.roles.all())])


auditlog.register(
    User,
    m2m_fields=['groups', 'user_permissions'],
    mask_fields=['password'],
    exclude_fields=['last_login'],
)


class Merchant(models.Model):
    name = models.CharField(max_length=150)
    infrastructure = models.CharField(
        max_length=60,
        choices=[
            ('betco', 'Betconstruct'),
        ]
    )
    currency = models.ForeignKey('commerce.Currency', on_delete=models.CASCADE)
    main_domain = models.CharField(max_length=300)
    is_transaction_fetching_active = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


auditlog.register(
    Merchant,
    # m2m_fields=['groups', 'user_permissions'],
    # mask_fields=['password'],
    exclude_fields=['created_at', 'updated_at'],
)


class InfrastructureCredential(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)

    email = models.CharField(max_length=400)
    password = models.CharField(max_length=200)
    otp_secret = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


auditlog.register(
    InfrastructureCredential,
    # m2m_fields=['groups', 'user_permissions'],
    mask_fields=['password', 'otp_secret'],
    exclude_fields=['created_at', 'updated_at'],
)


class Role(models.Model):
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    permissions = models.ManyToManyField('auth.Permission')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


auditlog.register(
    Role,
    m2m_fields=['permissions'],
    exclude_fields=['created_at', 'updated_at'],
)


class InSiteNotification(models.Model):
    TYPE_GENERAL = 'general'
    TYPE_USER_SPECIFIC = 'user_specific'

    start_showing_at = models.DateTimeField(null=True, blank=True)
    end_showing_at = models.DateTimeField(null=True, blank=True)

    subject = models.CharField(max_length=200)
    body = models.TextField()

    is_active = models.BooleanField(default=True)

    type = models.CharField(
        max_length=40,
        choices=[
            (TYPE_GENERAL, _('General')),
            (TYPE_USER_SPECIFIC, _('User Specific'))
        ],
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


auditlog.register(
    InSiteNotification,
    exclude_fields=['created_at', 'updated_at'],
)


class InSiteNotificationUserInteraction(models.Model):
    notification = models.ForeignKey(
        InSiteNotification,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    # start_showing_at = models.DateTimeField(null=True, blank=True)
    # end_showing_at = models.DateTimeField(null=True, blank=True)
    #
    # subject = models.CharField(max_length=200, null=True, blank=True)
    # body = models.TextField(null=True, blank=True)

    is_deleted = models.BooleanField(default=False)

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [('notification', 'user')]


auditlog.register(
    InSiteNotificationUserInteraction,
    exclude_fields=['created_at', 'updated_at']
)

