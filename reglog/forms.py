from django import forms
from reglog.models import userdetails,product
class users(forms.ModelForm):
    class Meta:
        model=userdetails
        fields="__all__"

class subusers(users):
    class Meta:
        model=userdetails
        fields=["name","mobile"]

class newform(forms.Form):
    name=forms.CharField()
    password=forms.CharField()

class Exform(forms.Form):
    userid=forms.CharField()
    password=forms.CharField()
    cpassword=forms.CharField()


class productforms(forms.ModelForm):
    class Meta:
        model=product
        fields=('name','image','price','description')


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']



