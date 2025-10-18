from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
    path('auth/login/', views.obtain_auth_token),
]
