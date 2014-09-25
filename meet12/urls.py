from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'meet12.views.IndexView', name='index'),

    url(r'^admin/', include(admin.site.urls)),
)
