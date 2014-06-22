from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', include('pop_vote.urls',
                                          namespace='pop_vote')),
                   )
