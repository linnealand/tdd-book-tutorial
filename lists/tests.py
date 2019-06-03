from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page # home page view function

# Create your tests here.
class HomePageTest(TestCase):

    # Django Test Client implicitly tests this

    '''
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/') # resolve URL '/' and find what view function it maps to (should be home_page)
        self.assertEqual(found.func, home_page)
    '''

    # test implementation, not constants
    '''
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request) # pass request to home_page view
        html = response.content.decode('utf8') # extract raw bytes & convert
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))
    '''

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'}) # form data to send
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
