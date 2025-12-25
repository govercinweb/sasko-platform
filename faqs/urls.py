from django.urls import path, include
from rest_framework import routers

from faqs import views

router = routers.DefaultRouter()
router.register('faqs', views.FaqViewSet, 'faqs')

urlpatterns = [
    path('', include(router.urls)),
]
