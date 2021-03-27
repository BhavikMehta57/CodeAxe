from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from carserviceapp.models import User,Shop,Booking

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='Required')

    class Meta:
        model = User
        fields = ['email','first_name','last_name','phone_number','password1','password2']

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['shop_name','owner_name','shop_email','shop_contact','owner_contact','shop_location','vehicle_servicing_charge',
        'vehicle_breakdown_Support_charge','vehicle_parts_Replacement_charge','vehicle_modification_charge','body_repair_and_repainting_charge','shop_image']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['services_required']