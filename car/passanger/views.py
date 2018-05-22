from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import View
from django.contrib import messages

# Create your views here.


def home(request):

    title = 'Passenger'
    return render(request, 'passenger/home.html', {'title': title})
