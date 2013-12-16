from django.contrib import admin
from pages.models import Page

class PageAdmin(admin.ModelAdmin):
    """ Page's ModelAdmin """
    fields = ['name', 'cotents']

admin.site.register(Page, PageAdmin)
