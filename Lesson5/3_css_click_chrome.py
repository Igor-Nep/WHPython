from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Откройте страницу http://uitestingplayground.com/classattr
driver.get('http://uitestingplayground.com/classattr')
#Кликните на синюю кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
for i in range(0, 3):
    blue_button.click()
