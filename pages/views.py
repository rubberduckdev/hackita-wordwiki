# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic

from pages.models import Page

class WordIndexView(generic.ListView):
    template_name = 'pages/page_list.html'
    context_object_name = 'words_list'

    def get_queryset(self):
        """ Return the words index """
        return Page.objects.all()
