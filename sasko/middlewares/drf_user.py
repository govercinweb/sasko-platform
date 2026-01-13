from django.contrib.auth.models import AnonymousUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class DRFUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.authenticators = (TokenAuthentication(), )

    def __call__(self, request):
        user = getattr(request, "user", None)

        if not user or isinstance(user, AnonymousUser) or not user.is_authenticated:
            for authenticator in self.authenticators:
                try:
                    result = authenticator.authenticate(request)
                except AuthenticationFailed:
                    result = None

                if result is not None:
                    request.user, request.auth = result
                    # 👇 mark as already authenticated for DRF
                    request._preauth_user = request.user
                    request._preauth_auth = request.auth
                    break

        return self.get_response(request)
