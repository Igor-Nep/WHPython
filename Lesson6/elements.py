from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

driver.get('https://ya.ru')
element = driver.find_element(By.CSS_SELECTOR, '#text')
element.send_keys('t', 'est Skypro')
driver.find_element(By.CSS_SELECTOR, 'body > main > div.body__content > form > div.search3__inner > button').click()
sleep(5)
driver.quit()