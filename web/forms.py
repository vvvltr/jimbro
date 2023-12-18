from django import forms
from django.contrib.auth import get_user_model

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