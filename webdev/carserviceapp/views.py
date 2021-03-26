import os
from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from carserviceapp.forms import RegistrationForm
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
