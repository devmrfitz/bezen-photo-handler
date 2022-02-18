
from rest_framework import viewsets


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
