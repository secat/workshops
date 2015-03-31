from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'catalog.views.home', name='home'),

    url(r'^parts/', include('parts.urls')),

    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^admin/', include(admin.site.urls)),
)
