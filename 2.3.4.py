from selenium import webdriver
from math import *

def f(x):
    return log(abs(12*sin(x)))

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(10)

browser.get('http://suninjuly.github.io/alert_accept.html')
browser.find_element_by_xpath('//button[@type="submit"]').click()
alert = browser.switch_to.alert
alert.accept()

x = browser.find_element_by_xpath('//span[@id="input_value"][text()]').text
r = f(int(x))
browser.find_element_by_css_selector('#answer').send_keys('%s' % r)
browser.find_element_by_xpath('//button[@type="submit"]').click()