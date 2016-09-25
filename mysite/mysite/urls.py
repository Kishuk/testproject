from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^fibonacci/', include('fibonacci.urls')),
    url(r'^admin/', include(admin.site.urls)),
)