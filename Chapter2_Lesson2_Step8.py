﻿from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
	
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("R")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("M")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("@.com")
    #input4 = browser.find_element_by_name("file").click()
    #input4.send_keys("")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element = browser.find_element_by_name("file")
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()