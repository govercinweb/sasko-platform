from django.urls import path, include
from rest_framework import routers

from commerce import views

router = routers.DefaultRouter()
router.register('orders', views.OrdersModelViewSet, 'orders')
router.register('sellables', views.SellablesViewSet, 'sellables')
router.register('currencies', views.CurrenciesViewSet, 'currencies')

urlpatterns = [
    path('', include(router.urls)),
]
