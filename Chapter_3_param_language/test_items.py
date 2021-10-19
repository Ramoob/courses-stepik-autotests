"""Файл для теста
Тест запускать командой: pytest --language=es test_items.py
"""
import time

def test_find_add_to_cart_button(browser):
	browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
	time.sleep(5)
	button = browser.find_element_by_class_name('btn-add-to-basket').is_displayed()
	assert button, "Кнопка 'Добавить в корзину' на странице присутствует"
