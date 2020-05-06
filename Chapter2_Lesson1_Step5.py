from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    input5 = browser.find_element_by_id("answer")
    input5.send_keys(y)

    input2 = browser.find_element_by_id("robotCheckbox").click()
    input3 = browser.find_element_by_id("peopleRule").click()
    input4 = browser.find_element_by_id("robotsRule").click()

    Button = browser.find_element_by_tag_name("button").click()

finally:
    # успеваем скопировать код за 30 секунд
     time.sleep(10)
    # # закрываем браузер после всех манипуляций
     browser.quit()

# не забываем оставить пустую строку в конце файла