from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

#Откройте страницу http://the-internet.herokuapp.com/entry_ad
driver.get('http://the-internet.herokuapp.com/entry_ad')
sleep(2)
#Кликните на Close
close_button = driver.find_element(By.CSS_SELECTOR, 'div.modal-footer')
close_button.click()
