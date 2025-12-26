import datetime

from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response

from django.db.models import Q, Prefetch, OuterRef

from accounts.models import InSiteNotification, InSiteNotificationUserInteraction
from accounts.serializers import ProfileDetailUpdateSerializer, ChangePasswordSerializer, \
    InSiteNotificationSerializer
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
        ).order_by(
            '-created_at',
        ).distinct()

        filtered_notifications = filter(
            lambda n: not n.interactions or not n.interactions[0].is_deleted,
            notifications
        )
        return filtered_notifications

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        unread_count = len(
            list(
                filter(
                    lambda n: not n['interactions'] or not n['interactions'][0]['is_read'],
                    response.data,
                )
            )
        )
        return Response({
            'unread_count': unread_count,
            'results': response.data,
        })
