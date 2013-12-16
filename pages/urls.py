"""
pages urls
"""

from django.conf.urls import patterns, url

from pages import views

urlpatterns = patterns('',
    url(r'^word/$', views.index, name='index'),
)
