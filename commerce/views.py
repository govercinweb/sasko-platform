import django_filters
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from commerce.models import Order, Sellable, Currency
from commerce.serializers import OrderSerializer, OrderCancelSerializer, OrderDeleteSerializer, SellableSerializer, \
    CurrencySerializer


class OrdersModelViewSet(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         # mixins.UpdateModelMixin,
                         # mixins.DestroyModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    queryset = Order.objects.filter(is_deleted=False).prefetch_related('orderitem_set')
    serializer_class = OrderSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('is_cancelled',)

    # def dispatch(self, request, *args, **kwargs):
    #     import time
    #     time.sleep(1)
    #     return super().dispatch(request, *args, **kwargs)

    @action(detail=True, methods=['patch'], serializer_class=OrderCancelSerializer)
    def cancel_order(self, request, pk):
        order = self.get_object()
        serializer = self.get_serializer(data=request.data, instance=order)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'data': serializer.data})

    @action(detail=True, methods=['delete'], serializer_class=OrderDeleteSerializer)
    def delete_order(self, request, pk):
        order = self.get_object()
        serializer = self.get_serializer(data=request.data, instance=order)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'data': serializer.data})


class SellablesViewSet(
    # mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    # mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Sellable.objects.all()
    serializer_class = SellableSerializer


class CurrenciesViewSet(
    # mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    # mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
