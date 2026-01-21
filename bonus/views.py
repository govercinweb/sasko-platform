import django_filters
from rest_framework import viewsets, mixins

from bonus.models import BonusCategory, UserBlock
from bonus.serializers import BonusCategorySerializer, UserBlockSerializer


class BonusCategoryViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = BonusCategory.objects.all()
    serializer_class = BonusCategorySerializer

    def get_queryset(self):
        return super().get_queryset().filter(merchant=self.request.user.merchant)
from bonus.serializers import BonusCategorySerializer


class UserBlockViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = UserBlock.objects.all()
    serializer_class = UserBlockSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('is_active',)

    def get_queryset(self):
        return super().get_queryset().filter(merchant=self.request.user.merchant)
