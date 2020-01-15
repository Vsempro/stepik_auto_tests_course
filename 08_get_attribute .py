from selenium import webdriver
import time
import math

try:
    # Открыть страницу http://suninjuly.github.io/get_attribute.html. 
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Математическая функция от x
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    # Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    chest = browser.find_element_by_id('treasure')
    # Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x = chest.get_attribute('valuex')
    # Посчитать математическую функцию от x
    y = calc(x)
    # Ввести ответ в текстовое поле.
    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(str(y))

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
    