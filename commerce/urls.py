from django.urls import path, include
from rest_framework import routers

from commerce import views

router = routers.DefaultRouter()
router.register('orders', views.OrdersModelViewSet, 'orders')

urlpatterns = [
    path('', include(router.urls)),
]
