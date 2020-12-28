from django import forms
from client.models import ClientInformation

from reglog.forms import product
class LoginForm(forms.ModelForm):
    class Meta:

        model = ClientInformation
        fields = ("email", "password")




class productforms(forms.ModelForm):
    class Meta:
        model=product
        fields=('name','image','price','description','makername')