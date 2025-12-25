from django.urls import path, include

from api.views import obtain_expiring_auth_token

urlpatterns = [
    path('auth/login/', obtain_expiring_auth_token),
    path('accounts/', include('accounts.urls')),
    path('faqs/', include('faqs.urls')),
]
