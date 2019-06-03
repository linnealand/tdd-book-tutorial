from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page # home page view function

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') # resolve URL '/' and find what view function it maps to (should be home_page)
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request) # pass request to home_page view
        html = response.content.decode('utf8') # extract raw bytes & convert
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
