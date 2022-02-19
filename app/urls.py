from django.urls import path
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import RecordViewSet, get_image

router = SimpleRouter()
router.register(r'records', RecordViewSet)

urlpatterns = [
    path('image/<int:record_id>/', get_image, name='image'),
]

urlpatterns += router.urls
