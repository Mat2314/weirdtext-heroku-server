from django.urls import include
from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'encode', views.EncodeViewSet, basename="encode")
router.register(r'decode', views.DecodeViewSet, basename="decode")

urlpatterns = [
    url('', include(router.urls)),
]
