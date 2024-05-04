from selenium.webdriver.common.by import By

class EShop:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')
        self._driver.implicitly_wait(10)

    def login(self):
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    def to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
        self._driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a').click()

    def checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    def form(self):
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Igor')
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Nep')
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('355000')
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click() 

    def total(self):
        return self._driver.find_element(By.CLASS_NAME, 'summary_total_label').text                   

