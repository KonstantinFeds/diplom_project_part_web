import pytest
from selene import browser, be
from tests.page.cart_page import CartPage

cart_page = CartPage()


@pytest.fixture(scope='function')
def open_browser():
    browser.driver.maximize_window()
    browser.config.base_url = 'https://ural-auto.ru/'


@pytest.fixture(scope='function')
def go_to_the_catalog_dinamiki(open_browser):
    browser.open('/')
    browser.element('[title="Каталог"]').click()
    browser.element('a.nav-submenu__list-link_title[href="/catalog/dinamiki/"]').click()


@pytest.fixture(scope='function')
def accept_cookies(open_browser):
    browser.open('/')
    browser.element('.js-message-block__close').should(be.clickable).click()



    yield
    browser.quit()

