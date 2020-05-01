# from selenium import webdriver
# import math
# from time import sleep
#
# browser = webdriver.Chrome()
# browser.maximize_window()
#
# try:
#     browser.get('http://suninjuly.github.io/find_xpath_form')
#     # browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e) * 10000))).click()
#     input1 = browser.find_element_by_tag_name('input')
#     input1.send_keys("Ivan")
#     input2 = browser.find_element_by_name('last_name')
#     input2.send_keys("Petrov")
#     input3 = browser.find_element_by_class_name('city')
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element_by_id('country')
#     input4.send_keys("Russia")
#     button = browser.find_element_by_xpath("//button[text()='Submit']")
#     button.click()
# finally:
#     sleep(30)
#     browser.quit()

from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_css_selector('div.first_block input.first').send_keys('1')
    browser.find_element_by_css_selector('div.first_block input.second').send_keys('2')
    browser.find_element_by_css_selector('div.first_block input.third').send_keys('3')
    browser.find_element_by_css_selector('div.second_block input.first').send_keys('4')
    browser.find_element_by_css_selector('div.second_block input.second').send_keys('5')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
