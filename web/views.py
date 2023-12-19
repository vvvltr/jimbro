from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from web import forms
from web.models import User


# Create your views here.
def main_view(request):
    date = datetime.now().year
    return render(request, 'web/main.html', {
        "year": date,
    })


def registration_view(request):
    form = forms.RegistrationForm()
    success = False
    if request.method == 'POST':
        form = forms.RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data['username'], email=form.cleaned_data['email'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            success = True
            print(form.cleaned_data)

    return render(request, "web/registration.html", {
        "form": form,
        "success": success
    })


def authentication_view(request):
    form = forms.AuthenticationForm()
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, "Wrong input or there is no user with that username")
            else:
                login(request, user)
                return redirect("main")
    return render(request, "web/authentication.html", {
        "form": form
    })


def profile_view(request):
    return render(request, "web/profile.html")


def logout_view(request):
    logout(request)
    return redirect('main')


def add_exercise_view(request):
    form = forms.ExerciseForm()
    return render(request, "web/add_exercise.html", {"form": form})


def add_training_view(request):
    form = forms.TrainingForm()
    return render(request, "web/add_training.html", {"form": form})


def add_workout_view(request):
    form = forms.WorkoutForm()
    return render(request, "web/add_workout.html")
