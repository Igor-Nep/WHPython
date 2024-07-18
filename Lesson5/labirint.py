
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://labirint.ru')

search_locator = '#search-field'
search_input = driver.find_element(By.CSS_SELECTOR, search_locator)
search_input.send_keys('Python', Keys.RETURN)


books = driver.find_elements(By.CSS_SELECTOR, 'div.product-card')
print(len(books))
i=0
for book in books:
    
    title = '' #('div.product-card[data-name]')
    author = ''
    price = '' #('div.product-card[data-discount-price]')
    try:
        author = book.find_element(By.CSS_SELECTOR, 'div.product-card__author').text
    except:
        author = 'Автор не указан'

    try:
        title = book.find_element(By.CSS_SELECTOR, 'a.product-card__name').text
    except:
        title = 'Название не указано'   

    try:
        price = book.find_element(By.CSS_SELECTOR, 'div.product-card__price-current').text
    except:
        price = 'Цена не указана'    

       
    i += 1
    print(f'{i}. Книга "{title}" автор - {author}. Цена - {price}')
   
sleep(1) 