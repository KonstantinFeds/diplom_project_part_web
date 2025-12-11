import allure
import pytest
from selene import browser, be

import config
from tests.pages.locators import Locators
from utils import attach


@allure.title("настройка конфигурации браузера")
@pytest.fixture(scope="function", autouse=True)
def browser_config():
    browser.config.base_url = "https://ural-auto.ru/"
    browser.config.timeout = 10
    browser.config.window_width = 1495
    browser.config.window_height = 870


@allure.title("открытие сайта и обработка cookies")
@pytest.fixture(scope="function")
def open_site_without_cookies(browser_config):
    browser.open("/")
    browser.element(Locators.ACCEPT_COOKIES_BUTTON).should(be.clickable).click()

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    config.clear_allure_results()

    browser.quit()
