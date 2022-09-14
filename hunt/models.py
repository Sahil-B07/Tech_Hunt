from django.db import models

# Create your models here.
class Question(models.Model):
    q_id = models.AutoField
    question = models.CharField(max_length=5000)
    answer = models.CharField(max_length=1000)
    level = models.CharField(max_length=2)

class Team(models.Model):
    team_username = models.CharField(max_length=150)
    questions = models.CharField(max_length=100)
    time_started = models.TimeField()
    time_finished = models.TimeField()
    questions_answered = models.IntegerField()

    def __str__(self):
        return self.team_username