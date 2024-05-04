from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from Pages.MainPage import MainPage
from Pages.ResultPage import ResultPage
from Pages.CartPage import CartPage

def test_counter():
    driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(driver)
    main_page.set_cookie_policy()
    main_page.search('python')
    result_page = ResultPage(driver)
    to_be = result_page.add_books()
    cart_page = CartPage(driver)
    cart_page.get()
    as_is = cart_page.get_counter()
    assert to_be == as_is
