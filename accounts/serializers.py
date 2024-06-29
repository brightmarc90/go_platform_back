from rest_framework import serializers
from .models import *

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'action', 'description']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password', 'username', 'is_superuser', 'is_staff', 'role']

class RolePemissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role_Permission
        fields = ['id', 'role', 'permission']