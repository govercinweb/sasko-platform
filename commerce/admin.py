from django.contrib import admin

from commerce.models import Sellable, Currency, ExchangeRate, Order, OrderItem


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


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order__order_number', 'id', 'order__merchant__name', 'sellable', 'count', 'created_at']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'order__merchant',
            'sellable',
        )


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('sellable')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'id', 'merchant', 'created_at', 'updated_at']

    inlines = [OrderItemInline]

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('merchant')
