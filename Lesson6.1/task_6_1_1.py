from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)
driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

def test_inform():
    driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys('Иван')
    driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys('Петров')
    driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys('Ленина, 55-3')
    driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys()
    driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys('Москва')
    driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys('Россия')
    driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys('test@skypro.com')
    driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys('+7985899998787')
    driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys('QA')
    driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys('SkyPro')
    driver.find_element(By.CSS_SELECTOR, 'button').click()
    
    zip_color = driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('background-color')
    attr_list = ['#first-name', '#last-name', '#address', '#city', '#country', '#e-mail', '#phone', '#job-position', '#company']
   
    for i in attr_list:
        attr_color = driver.find_element(By.CSS_SELECTOR, i).value_of_css_property('background-color')
        assert attr_color == 'rgba(209, 231, 221, 1)'

    assert zip_color == 'rgba(248, 215, 218, 1)'

driver.quit()
       