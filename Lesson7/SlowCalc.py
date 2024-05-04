from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
class SlowCalc:
    
    def __init__(self, driver):
      self._driver = driver
      self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
      self._driver.implicitly_wait(4)

    def delay(self, delay):
      self._driver.find_element(By.CSS_SELECTOR, '#delay').clear()
      self._driver.find_element(By.CSS_SELECTOR, '#delay').send_keys(delay)

    def contain(self):
      self._driver.find_element(By.XPATH, '//span[contains(text(), "7")]').click()
      self._driver.find_element(By.XPATH, '//span[contains(text(), "+")]').click()
      self._driver.find_element(By.XPATH, '//span[contains(text(), "8")]').click()
      self._driver.find_element(By.XPATH, '//span[contains(text(), "=")]').click()  

    def wait_result(self):
      WebDriverWait(self._driver, 50).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.screen'), "15"))
      return self._driver.find_element(By.CSS_SELECTOR, '.screen').text     
   
