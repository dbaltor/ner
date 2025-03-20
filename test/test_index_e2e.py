import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class E2ETests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.get('http://localhost:5000/')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_browser_title_contains_app_name(self):
        self.assertIn('Named Entity', self.driver.title)

    def test_page_heading_is_named_entity_finder(self):
        heading = self._find('heading').text
        self.assertEqual('Named Entity Finder', heading)

    def test_page_has_input_for_text(self):
        input_element = self._find('input-text')
        self.assertIsNotNone(input_element)

    def test_page_has_button_for_submitting_text(self):
        submit_button = self._find('find-button')
        self.assertIsNotNone(submit_button)

    def test_submitting_sentence_create_table(self):
        input_element = self._find('input-text')
        submit_button = self._find('find-button')
        input_element.send_keys('Portugal and Spain share a border in Europe')
        submit_button.click()
        table = self._find('ner-table')
        self.assertIsNotNone(table)

    def _find(self, val):
        return self.driver.find_element(by=By.CSS_SELECTOR, value=f'[data-test-id="{val}"]')
