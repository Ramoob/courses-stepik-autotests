from selenium import webdriver
import math
import time
import pyperclip

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name("button").click()
    confirm = browser.switch_to.alert
    confirm.accept()

    time.sleep(1)
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    input5 = browser.find_element_by_id("answer")
    input5.send_keys(y)

    Button = browser.find_element_by_tag_name("button").click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

finally:
    # успеваем скопировать код за 30 секунд
     time.sleep(10)
    # # закрываем браузер после всех манипуляций
     browser.quit()

# не забываем оставить пустую строку в конце файла