

from rest_framework import viewsets


from .serializers import RecordSerializer
from .models import Record


class RecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows records to be viewed or edited.
    """
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
