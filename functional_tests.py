from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8080')

        # Page title and header
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # Enter a to-do list item

        # Type into text box

        # Hit enter, page updates, page lists item

        # There is a text box to add another item

        # Page updates again, shows both items in list

        # Site generates a unique URL

if __name__ == '__main__':
    unittest.main(warnings='ignore')
