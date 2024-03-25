from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Откройте страницу http://the-internet.herokuapp.com/entry_ad
driver.get('http://the-internet.herokuapp.com/entry_ad')
sleep(2)
#Кликните на Close
close_button = driver.find_element(By.CSS_SELECTOR, '#modal > div.modal > div.modal-footer > p')
close_button.click()
sleep(2)