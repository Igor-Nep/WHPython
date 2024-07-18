from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
driver.get('https://demoqa.com/radio-button')
sleep(2)
yes_radio = driver.find_element(By.CSS_SELECTOR, '#yesRadio').is_enabled()
print(yes_radio)
no_radio = driver.find_element(By.CSS_SELECTOR, '#noRadio').is_enabled()
print(no_radio)
driver.get('https://demoqa.com/checkbox')
sleep(2)
ch_bx = driver.find_element(By.CSS_SELECTOR, 'input[type=checkbox]')

is_sl = ch_bx.is_selected()
print(is_sl)
ch_bx = driver.find_element(By.CSS_SELECTOR, 'input[type=checkbox]').click()
sleep(2)
is_sl = ch_bx.is_selected()
print(is_sl)
driver.quit()
