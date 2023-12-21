from django.contrib import admin
from django.urls import path

import web.views

urlpatterns = [
    path('', web.views.main_view, name='main'),
    path('signup', web.views.registration_view, name='sign up'),
    path('signin', web.views.authentication_view, name='sign in'),
    path('profile', web.views.profile_view, name='profile'),
    path('logout', web.views.logout_view, name='log out'),
    path('workouts/add', web.views.add_workout_view, name='add workout'),
    path('exercises/add', web.views.add_exercise_view, name='add exercise')
]
