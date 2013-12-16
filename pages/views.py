# Create your views here.

from django.models import HttpResponse
from django.template import RequestContext, loader

from pages.models import Page

def index(request):
    pages = Poll.objects.all()
    template = loader.get_template('pages/index.html')
    context = RequestContext(
        request,
        {'pages': pages},
    )
    return HttpResponse(template.render(context))
