from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from web.forms import RegistrationForm
from web.models import User


# Create your views here.
def main_view(request):
    date = datetime.now().year
    return render(request, 'web/main.html', {
        "year" : date
    })

def registration_view(request):
    form = RegistrationForm()
    success = False
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data['username'], email=form.cleaned_data['email'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            success=True
            print(form.cleaned_data)

    return render(request, "web/registration.html", {
        "form": form,
        "success" : success
    })