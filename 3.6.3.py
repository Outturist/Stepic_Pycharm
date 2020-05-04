from selenium import webdriver
import pytest
import time
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"]


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


class TestAnswers:

    def answer(self):
        return math.log(int(time.time()))

    @pytest.mark.parametrize('link', links)
    def test_links(self, browser, link):
        browser.maximize_window()
        browser.implicitly_wait(10)
        browser.get(f'{link}')
        ans = self.answer()
        browser.find_element_by_xpath('//textarea').send_keys(f'{ans}')
        browser.find_element_by_css_selector('.submit-submission').click()
        WebDriverWait(browser, 30).until(EC.presence_of_element_located, ((By.XPATH, '//div[@class="smart-hints__feedback hints__component hints__component_showed ember-view"]')))
        text = browser.find_element_by_xpath('//pre[text()]').text
        assert text == 'Correct!', 'Ответ не верный'
