from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^passenger_profile/(?P<username>[-_\w.]+)$',
        views.profile, name='profile'),
    url(r'^passenger_profile/(?P<username>[-_\w.]+)/update/$',
        views.update_profile, name='update_profile'),
]
