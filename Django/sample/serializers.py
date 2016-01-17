from rest_framework import serializers
from sample.models import SampleModel


class SampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SampleModel
        fields = ('id', 'name')