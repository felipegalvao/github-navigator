from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewUserTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_search_github(self):
        # User access the navigator URL
        self.browser.get(self.live_server_url + '/navigator')

        # User inputs search term in the search box and submit it
        search_text = 'python'
        input_search = self.browser.find_element_by_id('id_search_term')
        input_search.send_keys('python')
        input_search.send_keys(Keys.ENTER)
        self.browser.implicitly_wait(10)

        # User notices the search term in the title, and then sees the 5 repositories 
        # sorted by creation date
        page_title = self.browser.find_element_by_tag_name('h1').text
        self.assertEqual(page_title, search_text)
        repositories = self.browser.find_elements_by_class_name('div-repository')
        self.assertEqual(len(repositories), 5)
