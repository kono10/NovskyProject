from .models import Visual
from rest_framework import serializers


class VisualSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visual
        fields = ["name", "body", "pub_date"]
