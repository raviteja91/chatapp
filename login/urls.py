from django.conf.urls import patterns, include, url
from messages.simple import redirect_to
#from django.contrib import admin
#admin.autodiscover()
from login.views import *
 
urlpatterns = patterns('',
	url(r'^$', redirect_to, {'url': 'messages/'}),
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
    #url(r'^admin/', include(admin.site.urls)),
)
