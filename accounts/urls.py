from django.urls import path, include
from rest_framework import routers

from accounts import views

router = routers.DefaultRouter()
router.register('me', views.ProfileMe, 'me')
router.register('in_site_notifications', views.InSiteNotificationViewSet, 'in_site_notifications')
router.register('merchants', views.MerchantsViewSet, 'merchants')
router.register(
    'infrastructure_credentials',
    views.InfrastructureCredentialViewSet,
    'infrastructure_credentials',
)

urlpatterns = [
    path('', include(router.urls)),
    path('infrastructures/', views.InfrastructureView.as_view()),
    path('main_merchant/', views.MainMerchantForSuperUser.as_view()),
]
