from __future__ import absolute_import

from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<year>\d{4})/$', views.by_year, name='by_year'),
)
