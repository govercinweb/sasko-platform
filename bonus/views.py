from rest_framework import viewsets, mixins

from bonus.models import BonusCategory
from bonus.serializers import BonusCategorySerializer


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
