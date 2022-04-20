from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import math

link = "https://www.ozon.ru/product/krossovki-x-plode-488347347/?sh=Bcs8NAAAAA"

try:
    browser = webdriver.Chrome()
    browser.get(link)
	# добавляем товар в корзину
    add_button = browser.find_element_by_css_selector("div[data-widget='webAddToCart'] button")
    add_button.click()

    # открываем страницу второго товара
    browser.get("https://www.ozon.ru/product/krossovki-491952942/?sh=Bcs8NAAAAA")
	
    # добавляем товар в корзину
    add_button = browser.find_element_by_css_selector("div[data-widget='webAddToCart'] button")
    add_button.click()
	
	# тестовый сценарий
	# открываем корзину
    browser.get("https://www.ozon.ru/cart")
	
	# закрываем поп-ап
    close_popup = browser.find_element_by_css_selector("div.zb1 div.z4b button")
    close_popup.click()
	
	# ищем все добавленные товары
    goods = browser.find_elements_by_css_selector("div.a7t")
	
    # проверяем, что количество товаров равно 2
    assert len(goods) == 2
	

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()