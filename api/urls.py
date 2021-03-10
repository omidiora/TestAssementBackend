from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import PersonalViewSet
from django.conf import settings
from django.conf.urls.static import static




router = routers.DefaultRouter()
router.register('', PersonalViewSet)

urlpatterns = [
    path('personalinfo', include(router.urls))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
