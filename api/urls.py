from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import PersonalViewSet




router = routers.DefaultRouter()
router.register('user', PersonalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
