from selenium import webdriver
import time
import unittest


class registration(unittest.TestCase):

    def test_1(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://suninjuly.github.io/registration1.html")
        self.browser.find_element_by_css_selector('div.first_block input.first').send_keys('1')
        self.browser.find_element_by_css_selector('div.first_block input.second').send_keys('2')
        self.browser.find_element_by_css_selector('div.first_block input.third').send_keys('3')
        self.browser.find_element_by_css_selector('div.second_block input.first').send_keys('4')
        self.browser.find_element_by_css_selector('div.second_block input.second').send_keys('5')
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, f'Ожидаемый результат {"Congratulations! You have successfully registered!"}, фактический результат {welcome_text}')
        self.q()

    def test_2(self):
        self.browser = webdriver.Chrome()
        self.browser.get("http://suninjuly.github.io/registration2.html")
        self.browser.find_element_by_css_selector('div.first_block input.first').send_keys('1')
        self.browser.find_element_by_css_selector('div.first_block input.second').send_keys('2')
        self.browser.find_element_by_css_selector('div.first_block input.third').send_keys('3')
        self.browser.find_element_by_css_selector('div.second_block input.first').send_keys('4')
        self.browser.find_element_by_css_selector('div.second_block input.second').send_keys('5')
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = self.browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, f'Ожидаемый результат {"Congratulations! You have successfully registered!"}, фактический результат {welcome_text}')
        self.q()

    def q(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()