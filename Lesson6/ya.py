from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager 
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ff = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
edge = webdriver.Edge(service = EdgeService(EdgeChromiumDriverManager().install()))

def make_screenshot(driver):
    driver.maximize_window()
    driver.get('https://ya.ru')
    sleep(3)
    driver.save_screenshot('D:/ya_'+driver.name+'.png')
    driver.quit()

make_screenshot(chrome)
make_screenshot(ff)
make_screenshot(edge)   