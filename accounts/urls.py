from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

router = DefaultRouter()
router.register(r'roles', RoleViewSet, basename='role')
router.register(r'permissions', PermissionViewSet, basename='permission')

urlpatterns = [
    path('', include(router.urls)),
    path('role-perms/', Role_PermissionList.as_view(), name='role-perms-list'),
    path('role-perms/<int:pk>', Role_PermissionDetail.as_view(), name='role-perms-detail'),
]