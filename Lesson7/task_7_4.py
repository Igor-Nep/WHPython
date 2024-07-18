from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from EShop import EShop

def test_swaglabs():
    driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
    ES = EShop(driver)

    ES.login()
    ES.to_cart()
    ES.checkout()
    ES.form()
    total = ES.total()
    driver.close() 
    assert total == 'Total: $58.29'