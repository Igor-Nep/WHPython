from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

#Откройте страницу http://uitestingplayground.com/dynamicid
driver.get('http://uitestingplayground.com/dynamicid')
#Кликните на синюю кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, '.btn')
#запустить скрипт 3 раза
for i in range(0, 3):
    blue_button.click()

