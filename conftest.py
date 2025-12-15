import allure
from dotenv import load_dotenv
import pytest
from selene import browser, be
import config
from tests.pages_ui_web.locators import LocatorsWeb
from utils import attach


@pytest.fixture(scope="session")
def clean_allure_results():
    config.clear_allure_results()


def pytest_addoption(parser):
    """добавляет опцию командной строки --context"""
    parser.addoption(
        "--context",
        default="local_browser",  # значение по умолчанию
        help="Specify the test context",
    )


def pytest_configure(config):
    """настройка тестового окружения на основе переданного параметра --context"""
    context = config.getoption("--context")
    env_file_path = f".env.{context}"

    load_dotenv(dotenv_path=env_file_path)


@pytest.fixture(scope="function")
def context(request):
    """возвращение контекста из командной строки"""
    return request.config.getoption("--context")


@pytest.fixture(scope="function", autouse=True)
def browser_management(context):
    config.to_driver_options(context)

    yield

    attach.add_screenshot_selenoid(browser)
    attach.add_logs_selenoid(browser)
    attach.add_html_selenoid(browser)

    if context == "selenoid":
        attach.add_selenoid_video(browser)

    with allure.step("завершение сессии"):
        browser.quit()


@allure.title("открытие сайта и обработка cookies")
@pytest.fixture(scope="function")
def open_site_without_cookies():
    browser.open("/")
    browser.element(LocatorsWeb.ACCEPT_COOKIES_BUTTON).should(be.clickable).click()

    yield
