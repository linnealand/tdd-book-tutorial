from django.urls import resolve
from django.test import TestCase
from lists.views import home_page # home page view function

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') # resolve URL '/' and find what view function it maps to (should be home_page)
        self.assertEqual(found.func, home_page)
