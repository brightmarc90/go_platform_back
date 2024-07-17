from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all().order_by('id') 
    serializer_class = RoleSerializer

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all().order_by('id') 
    serializer_class = PermissionSerializer
    
class Role_PermissionList(generics.ListCreateAPIView):
    queryset = Role_Permission.objects.all().order_by('id') 
    serializer_class = RolePemissionSerializer

class Role_PermissionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role_Permission.objects.all()
    serializer_class = RolePemissionSerializer

@swagger_auto_schema(
    methods=['post'],
    operation_description="Créer ou inscrire un nouvel utilisateur",
    request_body=CustomUserSerializer,
    responses={201: CustomUserListSerializer},
)
@api_view(["POST"])
def signup_user(request):
    role = Role.objects.get(name = "Joueur")
    request.data["role"] = role.id
    request.data["username"] = request.data["username"].lower()
    request.data["email"] = request.data["email"].lower()
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = CustomUser.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        serializer = CustomUserListSerializer(user)
        return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    methods=['post'],
    operation_description="Authentifier un utilisateur",
    responses={200: CustomUserListSerializer},
)
@api_view(["POST"])
def login_user(request):
    user = get_object_or_404(CustomUser, username=request.data['username'].lower())
    if not user.check_password(request.data['password']):
        return Response({"detail": "Non trouvé"}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = CustomUserListSerializer(user)
    return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK)

@swagger_auto_schema(
    methods=['post'],
    operation_description="Déconnecter un utilisateur",
    responses={200: "No content"},
)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def logout_user(request):
    try:
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({"detail": "Déconnecté"}, status=status.HTTP_200_OK)
    except Token.DoesNotExist:
        return Response({"detail": "Token introuvable"}, status=status.HTTP_400_BAD_REQUEST)
    
class CustomUserList(generics.ListAPIView):
    queryset = CustomUser.objects.all().order_by('id') 
    serializer_class = CustomUserListSerializer

class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer