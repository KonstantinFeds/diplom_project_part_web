import allure
from dotenv import load_dotenv
import pytest
from selene import browser, be
import config
from tests.pages.locators import Locators
from utils import attach

@allure.title('очистка allure отчета от старых результатов')
@pytest.fixture(scope='session')
def clean_allure_results():

    config.clear_allure_results()

def pytest_addoption(parser):
    """Добавляет опцию командной строки --context"""
    parser.addoption(
        "--context",
        default="selenoid",  # значение по умолчанию
        help="Specify the test context",
    )


def pytest_configure(config):

    context = config.getoption("--context")
    env_file_path = f".env.{context}"

    load_dotenv(dotenv_path=env_file_path)

@allure.title('возвращение контекста из командной строки')
@pytest.fixture(scope="function")
def context(request):
    return request.config.getoption("--context")

@allure.title('настройка конфигураций для управления браузером')
@pytest.fixture(scope="function", autouse=True)
def browser_management(context):
    # Настраиваем браузер через config.py
    config.to_driver_options(context)

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)

    if context == 'selenoid':
        attach.add_video(browser)

    browser.quit()

@allure.title('открытие сайта и обработка cookies')
@pytest.fixture(scope="function")
def open_site_without_cookies():
    browser.open("/")
    browser.element(Locators.ACCEPT_COOKIES_BUTTON).should(be.clickable).click()

    yield

