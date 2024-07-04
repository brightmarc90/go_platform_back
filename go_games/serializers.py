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

class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = ['id', 'num_move', 'color', 'position', 'game']

class GameListSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    black_player = PlayerSerializer(read_only=True)
    white_player = PlayerSerializer(read_only=True)
    moves = MoveSerializer(many=True, read_only=True)
    class Meta:
        model = Game
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class TsumegoListSerializer(serializers.ModelSerializer):
    submitter = CustomUserSerializer(read_only=True)
    class Meta:
        model = Tsumego
        fields = ['id', 'problem_desc', 'description', 'status', 'difficulty', 'submitter']

class TsumegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tsumego
        fields = ['id', 'problem_desc', 'description', 'status', 'difficulty', 'submitter']