from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from BoniElements import BoniElements


def test_inform():
    driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
    BE = BoniElements(driver)
    BE.input_name('Иван')
    BE.input_last_name('Петров')
    BE.input_address('Ленина, 55-3')
    BE.input_zip('')
    BE.input_city('Москва')
    BE.input_country('Россия')
    BE.input_email('test@skypro.com')
    BE.input_phone('+7985899998787')
    BE.input_job('QA')
    BE.input_company('SkyPro')
    BE.click_submit()

    green = BE.color_green()
    red = BE.color_red()
    assert red == 'rgba(248, 215, 218, 1)' and green == 'rgba(209, 231, 221, 1)'  

    
    

    



       