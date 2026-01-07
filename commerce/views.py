from rest_framework import viewsets

from commerce.models import Order
from commerce.serializers import OrderSerializer


class OrdersModelViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.filter(is_deleted=False).prefetch_related('orderitem_set')
    serializer_class = OrderSerializer

    def dispatch(self, request, *args, **kwargs):
        import time
        time.sleep(1)
        return super().dispatch(request, *args, **kwargs)
