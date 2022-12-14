from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'imageupload', views.ImageUploadViewSet)

urlpatterns = [
    path('face', include(router.urls)),
]