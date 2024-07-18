from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))

driver.get('http://ya.ru')

current_title = driver.title
url = driver.current_url
print(url)

driver.quit()