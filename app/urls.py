from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import RecordViewSet, get_image, redirect_to_records

router = SimpleRouter()
router.register(r'records', RecordViewSet)

urlpatterns = [
    path('image/<int:record_id>/', get_image, name='image'),
    path('', redirect_to_records),

]

urlpatterns += router.urls
