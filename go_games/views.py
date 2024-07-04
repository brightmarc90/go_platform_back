from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import *
from .serializers import *
# Create your views here.

class TsumegoList(generics.ListAPIView):
    queryset = Tsumego.objects.all().order_by('id') 
    serializer_class = TsumegoListSerializer

class TsumegoCreate(generics.CreateAPIView):
    queryset = Tsumego.objects.all()
    serializer_class = TsumegoSerializer

class TsumegoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tsumego.objects.all()
    serializer_class = TsumegoListSerializer

class GameList(generics.ListAPIView):
    queryset = Game.objects.all().order_by('id') 
    serializer_class = GameListSerializer

class GameCreate(generics.CreateAPIView): # checker si à garder
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameDetail(generics.RetrieveDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameListSerializer