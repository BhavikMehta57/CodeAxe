import os
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from .models import *
from carserviceapp.forms import RegistrationForm, ShopForm, BookingForm

from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def home_page(request):
    return render(request, 'homepage.html')

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            return redirect('login')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request,'registration/register.html',context)

def shop_view(request):
    form = ShopForm()
    context={}
    if request.POST:
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'registration/shopform.html', {'form': form})

def booking_view(request):
    shop_id_new = request.GET.get("shopId")
    hired_shop = Shop.objects.values_list(
        'shop_name',flat=True).get(shop_id=shop_id_new)
    shop_email = Shop.objects.values_list(
        'shop_email', flat=True).get(shop_id=shop_id_new)
    currentuser = request.user
    email = User.objects.values_list('email',flat=True).get(email=currentuser)
    phonenumber = User.objects.values_list('phone_number',flat=True).get(email=currentuser)
    firstname = User.objects.values_list('first_name',flat=True).get(email=currentuser)
    lastname = User.objects.values_list('last_name',flat=True).get(email=currentuser)
    form = BookingForm()
    if not request.user.is_anonymous:
        form = BookingForm()
        if request.method == 'POST':
            form = BookingForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                services = form.cleaned_data.get('services_required')
                subject = 'New Mechanic Request'
                message = f'Hi {hired_shop}, You have a new booking from {firstname} {lastname}.Services Required: {services}.Contact Details: Email - {email} , Phone Number - {phonenumber}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [shop_email ]
                send_mail( subject, message, email_from, recipient_list)
                return redirect('myaccount')
            else:
                return render(request, 'registration/booking.html', {'form': form})
        return render(request, 'registration/booking.html', {'form': form})
    else:
        return redirect("login")

def myaccount_view(request):
    current_user = request.user
    mybookings = Booking.objects.filter(customer=current_user)
    return render(request,'registration/myaccount.html',{'mybookings':mybookings})


def shops_view(request):
    shops = Shop.objects.all()
    context = {'shops': shops}
    return render(request,'registration/shops.html',context)