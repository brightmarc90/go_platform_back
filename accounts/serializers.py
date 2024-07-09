from rest_framework import serializers
from .models import *

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'is_admin']

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'action', 'description']

class CustomUserListSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'is_superuser', 'is_staff', 'role']

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'is_superuser', 'is_staff', 'role']

class RolePemissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role_Permission
        fields = ['id', 'role', 'permission']