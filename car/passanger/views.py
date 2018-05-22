from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import View
from django.contrib import messages

# Create your views here.


def home(request):

    title = 'Passenger'
    return render(request, 'passenger/home.html', {'title': title})


def profile(request, username):
    '''
    render passenger information
    '''
    user = User.objects.get(username=username)
    profile = PassengerProfile.objects.get(user=user)
    location = Location.objects.get(user=user)

    title = f"{user.username}"
    return render(request, 'passenger/profile.html', {"user": user, "profile": profile, "location": location})
