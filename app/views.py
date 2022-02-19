from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .serializers import RecordSerializer
from .models import Record
from .tasks import compress


class RecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows records to be viewed or edited.
    """
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def perform_create(self, serializer):
        obj_created = serializer.save()
        compress.delay(obj_created.id)


@api_view(['GET'])
def get_image(request, record_id):
    """
    API endpoint that redirects to the image of a record (image served by NGINX).
    """
    return redirect(Record.objects.get(id=record_id).photo.url)
