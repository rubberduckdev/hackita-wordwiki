"""

pages views

"""

from django.views import generic

from pages.models import Page

def index(request):
    pages = Page.objects.all()
    context = {'pages': pages}
    return render(request, 'pages/index.html', context)

'''
class ListView(generic.ListView):
    template_name = 'pages/page_list.html'
    context_object_name = 'words_list'

    def get_queryset(self):
        """ Return the words index """
        return Page.objects.all()
'''
