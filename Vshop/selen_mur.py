from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os

os.system('D:\stilsoft\rc-5.0.7_murom-5.0.7.718-desktop-win32-x64\murom-desktop.exe -devtools --args --remote-debugging-port=9515')

options = Options() 
print('init Options')
options.debugger_address = 'localhost:9515'
options.add_argument('ignore-certificate-errors')
print('Init port ')
#driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()), options = options) 
driver = webdriver.Chrome(options = options)
print('Set options')
#print(driver.title)
driver.find_element(By.CSS_SELECTOR, 'input[data-testid="login"]').send_keys('admin')


driver.quit()
