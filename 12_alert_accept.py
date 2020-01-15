from selenium import webdriver
import time
import math

try:
    # Открыть страницу http://suninjuly.github.io/alert_accept.html
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажать на кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element_by_id('input_value').text
    captcha = calc(int(x_element))
    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(captcha))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    