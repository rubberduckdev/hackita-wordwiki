"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from pages.models import Page


class PagesTest(TestCase):
    def test_create_pages(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        p = Page()
        p.name = 'hello'
        p.contents = 'Tlon uqbar obsis...'
        p.full_clean()
        p.save()
        self.assertEqual(1, Page.objects.count())
