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
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('signup/', signup_user, name='signup_user'),
    path('users/', CustomUserList.as_view(), name='users-list'),
    path('users/<int:pk>', CustomUserDetail.as_view(), name='users-detail')
]