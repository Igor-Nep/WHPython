from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

#Откройте страницу http://the-internet.herokuapp.com/inputs
driver.get('http://the-internet.herokuapp.com/inputs')

#Введите в поле текст 1000
search_input = driver.find_element(By.CSS_SELECTOR, '#content > div > div > div > input[type=number]')
search_input.send_keys('1000', Keys.RETURN)
sleep(3)

#Очистите это поле
search_input.clear()

#Введите в поле текст 999
search_input.send_keys('999', Keys.RETURN)
sleep(3)