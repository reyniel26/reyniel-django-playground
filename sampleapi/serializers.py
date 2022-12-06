from dataclasses import field
from rest_framework import serializers
from sampleapi.models import Item

class ItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

        