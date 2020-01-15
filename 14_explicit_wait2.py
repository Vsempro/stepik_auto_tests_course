from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

import math

try:
    # Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    home_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

    if home_price:
        # ННажать на кнопку "Book"
        button_book = browser.find_element_by_id('book')
        button_book.click()
    #Решить математическую задачу и отправить решение
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element_by_id('input_value').text
    captcha = calc(int(x_element))
    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(captcha))
    button_solve = browser.find_element_by_id('solve')
    button_solve.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
