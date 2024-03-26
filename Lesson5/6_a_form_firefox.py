from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

#Откройте страницу http://the-internet.herokuapp.com/login
driver.get('http://the-internet.herokuapp.com/login')

#В поле username введите значение tomsmith
username_input = driver.find_element(By.CSS_SELECTOR, '#username')
username_input.send_keys('tomsmith')

#В поле password введите значение SuperSecretPassword!
password_input = driver.find_element(By.CSS_SELECTOR, '#password')
password_input.send_keys('SuperSecretPassword!')

#Нажмите кнопку Login
login_button = driver.find_element(By.CSS_SELECTOR, '#login > button')
login_button.click()
