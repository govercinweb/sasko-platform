from rest_framework import viewsets
from rest_framework.response import Response

from accounts.serializers import ProfileMeSerializer


class ProfileMe(viewsets.ViewSet):
    def list(self, request):
        return Response(ProfileMeSerializer(request.user).data)
