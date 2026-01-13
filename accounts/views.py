import datetime

import django_filters
from django.utils import timezone
from rest_framework import viewsets, mixins, views
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db.models import Q, Prefetch, OuterRef

from accounts.models import InSiteNotification, InSiteNotificationUserInteraction, Merchant
from accounts.serializers import ProfileDetailUpdateSerializer, ChangePasswordSerializer, \
    InSiteNotificationSerializer, InSiteNotificationChangeReadStatusSerializer, MerchantSerializer
from api.serializers import ProfileMeSerializer


class ProfileMe(viewsets.ViewSet):
    def list(self, request):
        return Response(ProfileMeSerializer(request.user).data)

    def patch(self, request):
        # update first_name and last_name
        user = request.user
        serializer = ProfileDetailUpdateSerializer(data=request.data, instance=user)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(ProfileMeSerializer(user).data)

    def post(self, request):
        # change password
        user = request.user
        serializer = ChangePasswordSerializer(data=request.data, instance=user)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(ProfileMeSerializer(user).data)


class InSiteNotificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InSiteNotification.objects.select_related(
        'user',
    ).filter(
        is_active=True,
    )
    serializer_class = InSiteNotificationSerializer

    def get_queryset(self):
        now = timezone.now()
        notifications = self.queryset.prefetch_related(
            Prefetch(
                'insitenotificationuserinteraction_set',
                queryset=InSiteNotificationUserInteraction.objects.filter(
                    user=self.request.user,
                ).distinct(),
                to_attr='interactions',
            ),
        ).filter(
            Q(created_at__gte=now - datetime.timedelta(days=90)),
            Q(user=self.request.user) | Q(type=InSiteNotification.TYPE_GENERAL),
            Q(start_showing_at__lte=now) | Q(start_showing_at__isnull=True),
            Q(end_showing_at__gte=now) | Q(end_showing_at__isnull=True),
        ).distinct()

        _notifications = filter(
            lambda n: not n.interactions or not n.interactions[0].is_deleted,
            notifications
        )
        _notifications = sorted(
            _notifications,
            key=lambda n: n.start_showing_at or n.created_at,
            reverse=True,
        )
        return _notifications

    @staticmethod
    def format_output(data):
        unread_count = len(
            list(
                filter(
                    lambda n: not n['interactions'] or not n['interactions'][0]['is_read'],
                    data,
                )
            )
        )
        return {
            'unread_count': unread_count,
            'results': data,
        }

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(self.format_output(response.data))

    @action(detail=False, methods=['patch'], serializer_class=InSiteNotificationChangeReadStatusSerializer)
    def change_read_status(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(self.format_output(InSiteNotificationSerializer(instance=self.get_queryset(), many=True).data))


class MerchantsViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('is_active',)


class InfrastructureView(views.APIView):
    def get(self, request):
        return Response(Merchant.INFRASTRUCTURES)
