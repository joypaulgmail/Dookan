from django import forms
from client.models import ClientInformation
class LoginForm(forms.ModelForm):
    class Meta:

        model = ClientInformation
        fields = ("email", "password")




