from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    # Открыть страницу http://SunInJuly.github.io/execute_script.html.
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Считать значение для переменной x.
    x_element = browser.find_element_by_id('input_value').text

    # Математическая функция от x
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y_element = calc(int(x_element))

    # Проскроллить страницу вниз.
    input_tag = browser.find_element_by_tag_name("input")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_tag)

    #Ввести ответ в текстовое поле.
    input_tag.send_keys(str(y_element))

    # Отметить checkbox "I'm the robot".
    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()

    # Выбрать radiobutton "Robots rule!".
    checkbox = browser.find_element_by_css_selector("#robotsRule")
    checkbox.click()

    # Нажать на кнопку Submit.btn
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()