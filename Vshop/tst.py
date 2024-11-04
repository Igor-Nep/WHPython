from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")


driver = webdriver.Chrome(options=chrome_options)

#driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
driver.get('https://www.youtube.com/')
sleep(10)
driver.find_element(By.CSS_SELECTOR, '#search').send_keys('Соболев Илья')

driver.find_element(By.CSS_SELECTOR, '#search').send_keys(Keys.RETURN)
sleep(20)




