import datetime

from django.conf import settings
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed


class ExpiringTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        try:
            token = self.get_model().objects.get(key=key)
        except self.get_model().DoesNotExist:
            raise AuthenticationFailed('Invalid token')

        if not token.user.is_active:
            raise AuthenticationFailed('User inactive or deleted')

        # This is required for the time comparison
        utc_now = timezone.now()

        if token.created < utc_now - datetime.timedelta(hours=settings.DRF_AUTH_TOKEN_LIFE_IN_HOURS):
            raise AuthenticationFailed('Token has expired')

        return token.user, token
