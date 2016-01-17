from rest_framework import viewsets
from rest_framework import permissions

from sample.models import SampleModel
from sample.serializers import SampleSerializer


class SampleViewSet(viewsets.ModelViewSet):
    queryset = SampleModel.objects.all()
    serializer_class = SampleSerializer
    permission_classes = (permissions.AllowAny, )

