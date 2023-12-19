from datetime import datetime

from django import forms
from django.contrib.auth import get_user_model

from web import models

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
    date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type": "datetime-local"}))
    user = User
    class Meta:
        model = models.Workout
        fields = ('date', 'user')

class TrainingForm(forms.ModelForm):
    title = forms.CharField()
    reps = forms.IntegerField()
    sets = forms.IntegerField()


class ExerciseForm(forms.ModelForm):
    muscles = {
        'chest',
        'back',
        'arms',
        'abdominals',
        'legs',
        'shoulders'
    }
    muscle_group = forms.ChoiceField(choices=muscles)
    class Meta:
        model = models.Exercise
        fields = ('title', 'muscle_group')
