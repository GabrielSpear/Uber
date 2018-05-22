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


def update_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = PassengerProfileForm(
            request.POST, instance=request.user.passengerprofile, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request, ('Your profile was successfully updated!'))
            return HttpResponseRedirect("/passenger/passenger_profile/%s" % user.username)
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = PassengerProfileForm(
            instance=request.user.passengerprofile)
