from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.http import HttpResponse

import pages.views


def main(request):
    return HttpResponse('<img src="{{ STATIC_URL }}Gunter.jpg" title="Quack!" alt="Quack!"')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wordwiki.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', main, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^word/[a-z]+$', main, name='pages'),
    #url(r'^word/[a-z]+/edit', '', name='pages'),
    #url(r'^add-word/', '', name='pages'),
    url(r'^word/$', pages.WordIndexView.as_view()),
    #url(r'^word/$', pages.views.index, name='word'),
)
