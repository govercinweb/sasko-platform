from rest_framework import viewsets
from rest_framework.response import Response

from accounts.serializers import ProfileDetailUpdateSerializer, ChangePasswordSerializer
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
