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

def open_labirint(): #перейти на сайт
    driver.get('https://www.labirint.ru/')
    driver.implicitly_wait(4)
    driver.add_cookie(cookie)

def search(word): #найти все по слову
    driver.find_element(By.CSS_SELECTOR,'#search-field').send_keys(word)
    driver.find_element(By.CSS_SELECTOR,'#searchform > div.b-search-e-input-wrapper > button').click()

def add_books(): #добавить все книги в корзину + счетчик
    buy_buttons = driver.find_elements(By.CSS_SELECTOR,'a._btn.btn-tocart.buy-link')
    driver.implicitly_wait(6)
    counter = 0
    for btn in buy_buttons:
        btn.click()
        counter += 1
    return counter    

def goto_cart():  #перейти в корзину
    driver.get('https://www.labirint.ru/cart')

def get_cart_counter(): #провериь счетчик товаров == числу товаров    
    txt = driver.find_element(By.CSS_SELECTOR, "a[data-event-label='myCart']").find_element(By.CSS_SELECTOR, 'b').text 
    return int(txt)

def test_counter():
    open_labirint()
    search('python')
    added = add_books()
    goto_cart()
    cart_counter = get_cart_counter()
    assert cart_counter == added
