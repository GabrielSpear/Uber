from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

app_name = 'driver'

urlpatterns = [
    url(r'^(?P<username>[-_\w.]+)$', views.home, name='home'),
    url(r'^profile/(?P<username>[-_\w.]+)$',
        views.profile, name='profile_view'),
    url(r'^profile/(?P<username>[-_\w.]+)/update/$',
        views.update_profile, name='update_profile_view'),
    url(r'^location/(?P<username>[-_\w.]+)/update/$',
        views.update_location, name='update_location_view'),
    url(r'^find_passenger/$', views.find_passenger, name='find_passenger'),
    url(r'^add-marker/$', views.add_marker, name='add_marker'),
    url(r'^comment/$', views.add_comment, name='add_comment'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
