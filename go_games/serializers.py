from rest_framework import serializers
from .models import *

class EventSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name']

class PlayerSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'name']

class GameSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'
    
class MoveSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Move
        fields = ['id', 'num_move', 'color', 'position', 'game']

class TsumegoSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Tsumego
        fields = ['id', 'problem_desc', 'description', 'status', 'difficulty', 'submitter']