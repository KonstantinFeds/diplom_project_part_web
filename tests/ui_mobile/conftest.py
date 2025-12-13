import os
import allure
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium.webdriver.chrome.options import Options as ChromeOptions
from utils import attach
from selenium.webdriver import Remote
import utils.file


@pytest.fixture(scope="function", autouse=True)
def mobile_management():

    load_dotenv(dotenv_path=utils.file.abs_path_from_project('.env.credentials'))


    with allure.step("Настройка конфигураций под android для BrowserStack"):
        options = ChromeOptions()

        bstack_capabilities = {
            "browserName": "chrome",
            "platformName": "android",
            "bstack:options": {
                "projectName": "First Python project",
                "buildName": "Android Chrome test",
                "sessionName": "BStack android crome test",
                "userName": os.getenv('USER_NAME_BSTACK'),
                "accessKey": os.getenv('ACCESS_KEY_BSTACK'),
                "deviceName": "Google Pixel 9",
                "platformVersion": "16.0",
                "realMobile": "true",
                "local": "false",
                "debug": "true",
                "networkLogs": "true"

            },
        }

    for key, value in bstack_capabilities.items():
        options.set_capability(key, value)


    driver = Remote(
        command_executor=f"https://{os.getenv('USER_NAME_BSTACK')}:{os.getenv('ACCESS_KEY_BSTACK')}@hub-cloud.browserstack.com/wd/hub",
        options=options)


    browser.config.driver = driver
    browser.config.timeout = 10.0

    yield

    session_id = browser.driver.session_id


    with allure.step("Закрытие сессии"):
        browser.quit()

    attach.add_bstack_video(session_id)




