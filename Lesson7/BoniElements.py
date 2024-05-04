from selenium.webdriver.common.by import By
class BoniElements:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
        self._driver.implicitly_wait(4)

    def input_name(self, name):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(name) 

    def input_last_name(self, l_name):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(l_name)

    def input_address(self, address):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys(address)  

    def input_zip(self, zip):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys(zip)

    def input_city(self, city):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys(city)

    def input_country(self, country):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys(country)

    def input_email(self, email):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(email)

    def input_phone(self, phone):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys(phone) 

    def input_job(self, job):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys(job)

    def input_company(self, company):
        self._driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys(company) 

    def click_submit(self):
        self._driver.find_element(By.CSS_SELECTOR, 'button').click()

    def color_red(self):
        match_red = self._driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property('background-color')
        return(match_red)
    
    def color_green(self):
        attr_list = ['#first-name', '#last-name', '#address', '#city', '#country', '#e-mail', '#phone', '#job-position', '#company']
        for i in attr_list:
            match_green = self._driver.find_element(By.CSS_SELECTOR, i).value_of_css_property('background-color')
            return(match_green)                