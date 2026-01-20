from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjUserAdmin
from django.contrib.sessions.models import Session
from django.utils.translation import gettext_lazy as _

from accounts.models import User, Merchant, InfrastructureCredential, Role, InSiteNotification, \
    InSiteNotificationUserInteraction


@admin.register(User)
class UserAdmin(DjUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", 'merchant')}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "roles",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "usable_password", "password1", "password2"),
            },
        ),
    )
    ordering = ['id']
    list_display = ("email", "merchant", "first_name", "last_name", "is_staff", "is_superuser", "is_active")
    search_fields = ("first_name", "last_name", "email")

    raw_id_fields = ['merchant']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('merchant').all()


class InfrastructureCredentialInline(admin.TabularInline):
    model = InfrastructureCredential
    extra = 1


@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_display = ['name', 'infrastructure', 'currency', 'main_domain', 'is_active']
    search_fields = ['name', 'main_domain']
    list_filter = ['currency']
    inlines = [InfrastructureCredentialInline]


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'merchant', 'created_at']
    search_fields = ['name', 'merchant__name']
    raw_id_fields = ['merchant']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('merchant').all()


@admin.register(InSiteNotification)
class InSiteNotificationAdmin(admin.ModelAdmin):
    list_display = ['subject', 'is_active', 'start_showing_at', 'created_at']


@admin.register(InSiteNotificationUserInteraction)
class InSiteNotificationUserInteractionAdmin(admin.ModelAdmin):
    pass


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']


@admin.register(InfrastructureCredential)
class InfrastructureCredentialAdmin(admin.ModelAdmin):
    list_display = ['email', 'merchant__name', 'created_at']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('merchant')
