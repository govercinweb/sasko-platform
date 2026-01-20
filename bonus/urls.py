from django.urls import path, include
from rest_framework import routers

from bonus import views

router = routers.DefaultRouter()
router.register('bonus_categories', views.BonusCategoryViewSet, 'bonus_categories')

urlpatterns = [
    path('', include(router.urls)),
]
