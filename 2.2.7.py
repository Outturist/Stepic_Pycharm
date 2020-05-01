from selenium import webdriver
import os
from time import  sleep

browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(10)

browser.get('http://dev.dadata.ru:8080/clean/')
browser.find_element_by_css_selector('#id_login-email').send_keys('andrey-andrey@mail.ru')
browser.find_element_by_css_selector('#id_login-password').send_keys('andrey-andrey@mail.ru')
browser.find_element_by_xpath('//div[@class="authorization_popup "]//input[@type="submit"]').click()

folder_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(folder_path, 'Clients.xlsx')
sleep(1)
browser.find_element_by_css_selector('#id_document').send_keys(file_path)


from selenium import webdriver
browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")