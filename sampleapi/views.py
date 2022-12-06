from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from sampleapi.models import Item
from .serializers import ItemSerializers
from sampleapi import serializers

# Create your views here.
@api_view(['GET'])
def get_data(request):
    sample_person = {'name':'Sheesh','age':'1 Million'}
    return Response(sample_person)

@api_view(['GET'])
def get_items(request):
    items = Item.objects.all()
    serializer = ItemSerializers(items,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_item(request):

    serializers = ItemSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

