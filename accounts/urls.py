from django.urls import path, include
from rest_framework import routers

from accounts import views

router = routers.DefaultRouter()
router.register('me', views.ProfileMe, 'me')
router.register('in_site_notifications', views.InSiteNotificationViewSet, 'in_site_notifications')

urlpatterns = [
    path('', include(router.urls)),
]
