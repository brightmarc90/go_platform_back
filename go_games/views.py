from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import *
# Create your views here.

class TsumegoList(generics.ListAPIView):
    queryset = Tsumego.objects.all()
    serializer_class = TsumegoListSerializer

class TsumegoCreate(generics.CreateAPIView):
    queryset = Tsumego.objects.all()
    serializer_class = TsumegoSerializer

class TsumegoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tsumego.objects.all()
    serializer_class = TsumegoListSerializer