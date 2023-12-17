from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Exercise(models.Model):
    title = models.CharField(max_length=50)
    muscle_group = models.CharField(max_length=50)

class Training(models.Model):
    title = models.CharField(max_length=50)
    reps = models.IntegerField(default=1)
    sets = models.IntegerField(default=1)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)

class Workout(models.Model):
    date = models.DateField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    training = models.ManyToManyField(Training)