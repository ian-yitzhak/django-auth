from django.shortcuts import render

from . forms import RegistrationForm
from django.contrib import messages

def registration(request):

    if request.method == 'POST':

        fm = RegistrationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request , 'registration success')


    else:

        fm = RegistrationForm()

    return render(request , 'registartion.html' , {'fm': fm})


def home(request):


    return render( request , 'home.html')