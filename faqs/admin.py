from django.contrib import admin

from faqs.models import FaqTag, Faq


@admin.register(FaqTag)
class FaqTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'is_active']
    ordering = ['order']


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer', 'order', 'is_active']
    list_filter = ['tag']
    ordering = ['order']
