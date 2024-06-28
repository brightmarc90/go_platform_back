from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name
    
class Player(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name
    
class Game(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    round = models.SmallIntegerField()
    result = models.CharField(max_length=32)
    w_p_rank = models.CharField(max_length=32, null=True)
    b_p_rank = models.CharField(max_length=32, null=True)
    comments = models.CharField(max_length=255, null=True)
    event = models.ForeignKey(Event, on_delete=models.PROTECT)
    black_player = models.ForeignKey(Player, on_delete=models.PROTECT, related_name="black_payer_id")
    white_player = models.ForeignKey(Player, on_delete=models.PROTECT, related_name="white_payer_id")

class Move(models.Model):
    num_move = models.IntegerField()
    color = models.CharField(max_length=1)
    position = models.CharField(max_length=2)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

class Difficulties(models.TextChoices):
    ELEMENTARY = 'ELM', 'Elementary'
    BEGINNER = 'BEG', 'Beginner'
    INTERMEDIATE = 'INT', 'Intermediate'
    ADVANCED = 'ADV', 'Advanced'

class Tsumego(models.Model):
    problem_desc = models.JSONField()
    description = models.TextField(null=True)
    status = models.BooleanField(default=False) # brouillon ou publié
    difficulty = models.CharField(max_length=3, choices=Difficulties.choices, null=True)