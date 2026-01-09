from rest_framework import serializers

from commerce.models import Order, OrderItem, Sellable, Currency
from utils.order_number import order_number_generator


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'code', 'symbol']


class SellableSerializer(serializers.ModelSerializer):
    currency_code = serializers.CharField(source='currency.code')
    currency_symbol = serializers.CharField(source='currency.symbol')

    class Meta:
        model = Sellable
        fields = [
            'id',
            'name',
            'price',
            'currency',
            'currency_code',
            'currency_symbol',
        ]


class OrderItemSerializer(serializers.ModelSerializer):
    # sellable = SellableSerializer()
    # price_currency = CurrencySerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'count', 'total_price', 'sellable', 'price_currency']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['sellable'] = SellableSerializer(instance.sellable).data
        data['price_currency'] = CurrencySerializer(instance.price_currency).data
        return data


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, source='orderitem_set')
    merchant_name = serializers.CharField(source='merchant.name', read_only=True)
    total_amount = serializers.DecimalField(
        source='total_in_default_currency',
        max_digits=10,
        decimal_places=2,
        read_only=True,
    )
    total_amount_currency_symbol = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            'id',
            'order_number',
            'order_items',
            'merchant_name',
            'created_at',
            'total_amount',
            'total_amount_currency_symbol',
            'merchant',
        ]
        extra_kwargs = {
            'order_number': {'read_only': True},
            'merchant': {'write_only': True},
        }

    def validate(self, attrs):
        attrs['order_number'] = order_number_generator()
        return attrs

    @staticmethod
    def get_total_amount_currency_symbol(obj):
        return Currency.DEFAULT_CURRENCY_SYMBOL

    def create(self, validated_data):
        order_items = validated_data.pop('orderitem_set')
        order = Order.objects.create(**validated_data)
        for item in order_items:
            item['order'] = order
            OrderItem.objects.create(**item)
        return order


class OrderCancelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'is_cancelled']
        extra_kwargs = {
            'is_cancelled': {'required': False},
        }

    def validate(self, attrs):
        if not attrs['is_cancelled']:
            raise serializers.ValidationError('This is can not be done!')
        return attrs


class OrderDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'is_deleted']
        extra_kwargs = {
            'is_deleted': {'required': False},
        }

    def validate(self, attrs):
        attrs['is_deleted'] = True
        return attrs
