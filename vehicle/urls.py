from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('car', CarViewSet)
# router.register('honda', HondaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('honda/', HondaViews.as_view())
]
