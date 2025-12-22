from rest_framework import viewsets
from rest_framework.response import Response

from accounts.serializers import ProfileDetailUpdateSerializer
from api.serializers import ProfileMeSerializer


class ProfileMe(viewsets.ViewSet):
    def list(self, request):
        return Response(ProfileMeSerializer(request.user).data)

    def post(self, request):
        user = request.user
        serializer = ProfileDetailUpdateSerializer(data=request.data, instance=user)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(ProfileMeSerializer(user).data)
