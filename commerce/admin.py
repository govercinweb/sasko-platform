from django.contrib import admin

from commerce.models import Sellable, Currency, ExchangeRate


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ['code', 'symbol', 'order']


@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ['from_currency', 'to_currency', 'date', 'rate']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('from_currency', 'to_currency')


@admin.register(Sellable)
class SellableAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'currency']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('currency')
