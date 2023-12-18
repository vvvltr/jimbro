from django.contrib import admin
from django.urls import path

import web.views


urlpatterns = [
    path('', web.views.main_view),
    path('signup', web.views.registration_view)
]
