from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import path, include

urlpatterns = [
    path('tsumegos/', TsumegoList.as_view(), name='tsumegos-list'),
    path('tsumegos-create/', TsumegoCreate.as_view(), name='tsumegos-create'),
    path('tsumegos/<int:pk>', TsumegoDetail.as_view(), name='tsumegos-detail')
   
]