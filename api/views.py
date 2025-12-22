import datetime

from django.utils import timezone
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from api.serializers import ProfileMeSerializer


class ObtainExpiringAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        if not created:
            # update the created time of the token to keep it valid
            token.created = timezone.now()
            token.save()

        user.last_login = timezone.now()
        user.save()

        return Response({'token': token.key, 'user': ProfileMeSerializer(user).data})


obtain_expiring_auth_token = ObtainExpiringAuthToken.as_view()
