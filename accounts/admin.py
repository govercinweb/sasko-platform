from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjUserAdmin
from django.utils.translation import gettext_lazy as _

from accounts.models import User, Merchant, InfrastructureCredential


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
    list_display = ("email", "first_name", "last_name", "is_staff")
    search_fields = ("first_name", "last_name", "email")

    raw_id_fields = ['merchant']


class InfrastructureCredentialInline(admin.TabularInline):
    model = InfrastructureCredential
    extra = 1


@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    list_display = ['name', 'infrastructure', 'currency', 'main_domain']
    search_fields = ['name', 'main_domain']
    list_filter = ['currency']
    inlines = [InfrastructureCredentialInline]
