import pytest
from selene import browser, be
from tests.page.cart_page import CartPage

cart_page = CartPage()


@pytest.fixture(scope="function")
def open_browser_and_accept_cookies():
    browser.driver.maximize_window()
    browser.open("https://ural-auto.ru/")
    # browser.config.base_url = 'https://ural-auto.ru/'
    browser.element(".js-message-block__close").should(be.clickable).click()

    yield
    browser.quit()
