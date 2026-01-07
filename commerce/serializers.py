from rest_framework import serializers

from commerce.models import Order, OrderItem, Sellable
from utils.order_number import order_number_generator


class SellableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sellable
        fields = ['id', 'name']


class OrderItemSerializer(serializers.ModelSerializer):
    sellable = SellableSerializer()

    class Meta:
        model = OrderItem
        fields = ['id', 'count', 'total_price', 'sellable']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, source='orderitem_set')

    class Meta:
        model = Order
        fields = ['id', 'order_number', 'order_items']
        extra_kwargs = {
            'order_number': {'read_only': True}
        }

    def validate(self, attrs):
        attrs['order_number'] = order_number_generator()
        return attrs
