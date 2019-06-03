from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])


    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8080')

        # Page title and header
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Enter a to-do list item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Type into text box
        inputbox.send_keys('Feed the cat')

        # Hit enter, page updates, page lists item
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Feed the cat')

        # There is still a text box, type into it
        inputbox.send_keys('Take a nap')

        # Hit enter, page updates again, page lists both items
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1: Feed the cat')
        self.check_for_row_in_list_table('2: Take a nap')
        '''
        self.assertTrue(any(row.text == '1: Feed the cat' for row in rows),
            f"New to-do item did not appear in table. Contents were:\n{table.text}"
        )
        '''

        # There is a text box to add another item
        self.fail('Finish the test!')

        # Page updates again, shows both items in list

        # Site generates a unique URL

if __name__ == '__main__':
    unittest.main(warnings='ignore')
