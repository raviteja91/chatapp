from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#from student.views import profile,logout_view
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teja.views.home', name='home'),
    # url(r'^teja/', include('teja.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}),
    #(r'^accounts/profile/$', 'student.views.profile'),
    (r'^messages/', include('messages.urls')),
    (r'^', include('login.urls')), 
    #(r'^logout/$',logout_view)
)

