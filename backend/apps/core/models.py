"""
Sasko.io Core Models
Temel modeller ve çoklu dil/para birimi desteği
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
import uuid


class User(AbstractUser):
    """Özelleştirilmiş kullanıcı modeli"""
    
    USER_TYPES = [
        ('operator_admin', _('Operator Admin')),
        ('operator_user', _('Operator User')),
        ('affiliate', _('Affiliate')),
        ('player', _('Player')),
        ('system_admin', _('System Admin')),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='player')
    preferred_language = models.CharField(max_length=10, default='tr')
    preferred_currency = models.CharField(max_length=10, default='USD')
    tenant = models.ForeignKey('Tenant', on_delete=models.CASCADE, null=True, blank=True)
    
    # Profil bilgileri
    phone = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=2, blank=True)  # ISO country code
    timezone = models.CharField(max_length=50, default='Europe/Istanbul')
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_activity = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'core_users'
        verbose_name = _('User')
        verbose_name_plural = _('Users')
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"


class Tenant(models.Model):
    """Multi-tenant desteği için kiracı modeli"""
    
    TENANT_TYPES = [
        ('premium_casino', _('Premium Casino')),
        ('standard_sportsbook', _('Standard Sportsbook')),
        ('startup_operator', _('Startup Operator')),
        ('enterprise', _('Enterprise')),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    tenant_type = models.CharField(max_length=30, choices=TENANT_TYPES)
    
    # Konfigürasyon
    api_version = models.CharField(max_length=10, default='v2.0')
    enabled_modules = models.JSONField(default=list)
    custom_settings = models.JSONField(default=dict)
    
    # Lisans bilgileri
    license_type = models.CharField(max_length=20, default='CURACAO')
    license_number = models.CharField(max_length=50, blank=True)
    
    # Durum
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'core_tenants'
        verbose_name = _('Tenant')
        verbose_name_plural = _('Tenants')
    
    def __str__(self):
        return self.name


class Currency(models.Model):
    """Para birimi modeli"""
    
    code = models.CharField(max_length=10, unique=True)  # USD, EUR, TRY, BTC
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    decimal_places = models.IntegerField(default=2)
    is_crypto = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    # Exchange rate (USD bazlı)
    exchange_rate = models.DecimalField(max_digits=20, decimal_places=8, default=1.0)
    last_updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'core_currencies'
        verbose_name = _('Currency')
        verbose_name_plural = _('Currencies')
        ordering = ['code']
    
    def __str__(self):
        return f"{self.code} - {self.name}"


class Language(models.Model):
    """Dil modeli"""
    
    code = models.CharField(max_length=10, unique=True)  # tr, en, de
    name = models.CharField(max_length=50)
    native_name = models.CharField(max_length=50)
    is_rtl = models.BooleanField(default=False)  # Right-to-left
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'core_languages'
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')
        ordering = ['code']
    
    def __str__(self):
        return f"{self.code} - {self.native_name}"
