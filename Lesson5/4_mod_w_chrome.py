from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#Откройте страницу http://the-internet.herokuapp.com/entry_ad
driver.get('http://the-internet.herokuapp.com/entry_ad')

#Кликните на Close
close_button = driver.find_element(By.CSS_SELECTOR, 'div.modal-footer')
close_button.click()
