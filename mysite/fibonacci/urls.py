from django.conf.urls import patterns, url

from fibonacci import views

urlpatterns = patterns('',
    # ex: /fibonacci/
    url(r'^$', views.print_fibonacci_series, name='print_fibonacci_series'),
)