from django import forms
from django.contrib.auth.forms import UserCreationForm

<<<<<<< HEAD
from models import User
=======
from carserviceapp.models import User

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='Required')

    class Meta:
        model = User
        fields = ['email','first_name','last_name','phone_number','password1','password2']
>>>>>>> eb5a199df0c3abc06b87d1a5c5613a81847c48eb
