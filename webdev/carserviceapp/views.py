import os
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .models import *
from carserviceapp.forms import RegistrationForm, ShopForm, BookingForm
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
    form = BookingForm()
    if str(request.user) != "AnonymousUser":
        currentuser = request.user
        user = User.objects.values_list(
            'email', flat=True).get(email=currentuser)

        form = BookingForm()
        if request.method == 'POST':
            form = BookingForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return render(request, 'registration/myaccount.html', {'form': form})
            else:
                return render(request, 'registration/booking.html', {'form': form})
        return render(request, 'registration/booking.html', {'form': form,'user': user})
    else:
        return redirect("login")

def myaccount_view(request):
    return render(request,'registration/myaccount.html')


def shops_view(request):
    shops = Shop.objects.all()
    context = {'shops': shops}
    return render(request,'registration/shops.html',context)