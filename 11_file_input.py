from selenium import webdriver
import time
import os

try:
    # Открыть страницу http://suninjuly.github.io/file_input.html
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнить текстовые поля: имя, фамилия, email
    firstname = browser.find_element_by_name('firstname')
    firstname.send_keys('Иван')
    lastname = browser.find_element_by_name('lastname')
    lastname.send_keys('Иванов')
    email = browser.find_element_by_name('email')
    email.send_keys('mail@mail.ru')

    # Загрузить файл. Файл должен иметь расширение .txt
    file = browser.find_element_by_name('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    file.send_keys(file_path)

    # Нажать на кнопку Submit.btn
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    