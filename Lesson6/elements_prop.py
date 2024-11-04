from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
driver.get('https://ya.ru')
usd = driver.find_element(By.CSS_SELECTOR, 'body > main > div.body__content > aside > section > a:nth-child(2)').text
tag = driver.find_element(By.CSS_SELECTOR, 'body > main > div.body__content > aside > section > a:nth-child(2)').tag_name
id = driver.find_element(By.CSS_SELECTOR, 'body > main > div.body__content > aside > section > a:nth-child(2)').id
atr = driver.find_element(By.CSS_SELECTOR, 'body > main > div.body__content > aside > section > a:nth-child(2)').get_attribute('href')
css_el = driver.find_element(By.CSS_SELECTOR, 'body > main > div.body__content > aside > section > a:nth-child(2)').value_of_css_property('color')
print(usd)
print(tag)
print(id)
print(atr)
print(css_el)
driver.quit()