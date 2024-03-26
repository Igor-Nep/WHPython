from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

#Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/
driver.get('http://the-internet.herokuapp.com/add_remove_elements/')

#Пять раз кликните на кнопку Add Element
search_addbutt = driver.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]')
for i in range(0, 5):
    search_addbutt.send_keys(Keys.ENTER)

#Соберите со страницы список кнопок Delete
ellist = driver.find_elements(By.CSS_SELECTOR, '.added-manually')

#Выведите на экран размер списка.
print(f'Размер списка элементов: {len(ellist)}')
