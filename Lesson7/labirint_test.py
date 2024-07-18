from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
#from time import sleep
driver = webdriver.Chrome()
cookie = {
    "name": "cookie_policy",
    "value": "1"
}


def test_inform():
    #перейти на сайт
    driver.get('https://www.labirint.ru/')
    driver.implicitly_wait(4)
    driver.add_cookie(cookie)
    #найти все по слову питон
    driver.find_element(By.CSS_SELECTOR,'#search-field').send_keys('python')
    driver.find_element(By.CSS_SELECTOR,'#searchform > div.b-search-e-input-wrapper > button').click()
    driver.implicitly_wait(4)
    #переключиться на таблицу
    #добавить все книги в корзину
    buy_buttons = driver.find_elements(By.CSS_SELECTOR,'a._btn.btn-tocart.buy-link')
    driver.implicitly_wait(6)
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1
    #перейти в корзину
    #провериь счетчик товаров == числу товаров
    
    driver.get('https://www.labirint.ru/cart')
    txt = driver.find_element(By.CSS_SELECTOR, "a[data-event-label='myCart']").find_element(By.CSS_SELECTOR, 'b').text
    assert counter == int(txt)

