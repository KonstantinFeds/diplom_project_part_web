import pytest
from selene import browser, be
from tests.pages.locators import Locators


@pytest.fixture(scope="function", autouse=True)
def browser_config():
    """Настройка конфигурации браузера"""
    browser.config.base_url = "https://ural-auto.ru/"
    browser.config.timeout = 10
    browser.config.window_width = 1495
    browser.config.window_height = 870


@pytest.fixture(scope="function")
def open_site_without_cookies(browser_config):
    """Открытие сайта и обработка куки"""
    browser.open("/")
    browser.element(Locators.ACCEPT_COOKIES_BUTTON).should(be.clickable).click()

    yield

    browser.quit()
