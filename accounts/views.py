from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import *
from .serializers import *

# Create your views here.
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class Role_PermissionList(generics.ListCreateAPIView):
    queryset = Role_Permission.objects.all()
    serializer_class = RolePemissionSerializer

class Role_PermissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role_Permission.objects.all()
    serializer_class = RolePemissionSerializer