from rest_framework import viewsets

from faqs.models import Faq
from faqs.serializers import FaqSerializer


class FaqViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Faq.objects.select_related(
        'tag',
    ).filter(
        is_active=True,
    ).order_by(
        'order',
    )
    serializer_class = FaqSerializer
