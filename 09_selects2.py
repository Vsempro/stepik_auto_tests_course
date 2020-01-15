from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    # Открыть страницу http://suninjuly.github.io/selects2.html 
    link = 'http://suninjuly.github.io/selects2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Посчитать сумму заданных чисел
    number1 = browser.find_element_by_id('num1').text
    number2 = browser.find_element_by_id('num2').text
    find_sum = int(number1) + int(number2)

    # Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(find_sum))

    # Нажать на кнопку Submit.btn
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    