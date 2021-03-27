from django import forms
from django.contrib.auth.forms import UserCreationForm

from carserviceapp.models import User,Shop

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='Required')

    class Meta:
        model = User
        fields = ['email','first_name','last_name','phone_number','password1','password2']

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['shop_name','owner_name','shop_email','shop_contact','owner_contact','shop_location','services','shop_image','service_charge']