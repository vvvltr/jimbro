from datetime import datetime

from django import forms
from django.contrib.auth import get_user_model

from web import models
from web.models import Training, Exercise

User = get_user_model()
class RegistrationForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password_confirm']:
            self.add_error("password", "Passwords do not match")
        return cleaned_data

    class Meta:
        user = User
        fields = ('username', 'email', 'password', 'password_confirm')

class AuthenticationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class WorkoutForm(forms.ModelForm):
    date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
                "format": "%Y-%m-%d %H:%M'"
            }))
    user = User
    ''' training = forms.ChoiceField(choices=[
        Training(user,
                 title='byceps curl standard set',
                 reps=12,
                 sets=3,
                 exercise=Exercise(
                     title='byceps curl',
                     muscle_group='arms(pull)')),
        Training(user,
                 title='pull ups standard set',
                 reps=12,
                 sets=3,
                 exercise=Exercise(
                     title='wide grip pull ups',
                     muscle_group='back and spine')
                 )]
    )'''
    # training = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)
    def save(self, commit=True):
        self.instance.user = self.initial['user']
        return super().save(commit)

    class Meta:
        model = models.Workout
        fields = ('date', 'user')

class TrainingForm(forms.ModelForm):
    # title = forms.CharField()
    reps = forms.IntegerField()
    sets = forms.IntegerField()
    exercises = forms.IntegerField()

    class Meta:
        model = models.Training
        fields = ('reps', 'sets', 'exercise')


class ExerciseForm(forms.ModelForm):
    muscle_group = forms.CharField()
    # muscle_group = forms.ChoiceField(choices=('arms', 'back', 'glutes', 'hamstrings'))
    class Meta:
        model = models.Exercise
        fields = ('title', 'muscle_group', 'image')
