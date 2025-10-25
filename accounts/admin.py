from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjUserAdmin
from django.utils.translation import gettext_lazy as _

from accounts.models import User, Merchant, InfrastructureCredential, Role


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
    list_display = ['name', 'infrastructure', 'currency', 'main_domain']
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
