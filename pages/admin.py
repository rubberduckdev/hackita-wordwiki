from django.contrib import admin
from pages.models import Page

class PageAdmin(admin.ModelAdmin):
    """ Page's ModelAdmin """
    fieldsets = [
        (None,
         {'fields': ['name']}
         ),
        ('Contents',
         {'fields': ['cotents'],
          'classes': ['collapse']}),
    ]

admin.site.register(Page, PageAdmin)
