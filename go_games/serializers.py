from rest_framework import serializers
from .models import *
from accounts.serializers import CustomUserSerializer

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name']

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
    
class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = ['id', 'num_move', 'color', 'position', 'game']

class TsumegoListSerializer(serializers.ModelSerializer):
    submitter = CustomUserSerializer(read_only=True)
    class Meta:
        model = Tsumego
        fields = ['id', 'problem_desc', 'description', 'status', 'difficulty', 'submitter']

class TsumegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tsumego
        fields = ['id', 'problem_desc', 'description', 'status', 'difficulty', 'submitter']