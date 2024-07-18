from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from SlowCalc import SlowCalc


def test_calc():
    driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
    SC = SlowCalc(driver)
    SC.delay(15)
    SC.contain()
    result = SC.wait_result()
    assert result == '15'

 