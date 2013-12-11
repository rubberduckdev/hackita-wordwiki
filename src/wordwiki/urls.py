from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.http import HttpResponse

from pprint import pprint, pformat

def main(request):
    return HttpResponse("Poop.<pre>{}</pre>".format(pformat(request)))

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wordwiki.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', main, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^word/[a-z]+$', main, name='pages'),
    #url(r'^word/[a-z]+/edit', '', name='pages'),
    #url(r'^add-word/', '', name='pages'),
    #url(r'^word/$', '', name='pages'),
)
