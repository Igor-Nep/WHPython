from selenium.webdriver.common.by import By
class ResultPage:

    def __init__(self, driver):
        self._driver = driver

    def add_books(self): #добавить все книги в корзину + счетчик
        buy_buttons = self._driver.find_elements(By.CSS_SELECTOR,'a._btn.btn-tocart.buy-link')
        self._driver.implicitly_wait(6)
        counter = 0
        for btn in buy_buttons:
            btn.click()
            counter += 1
        return counter     
