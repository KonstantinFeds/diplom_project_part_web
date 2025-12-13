import os
import shutil
from pathlib import Path

from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import utils.file


def clear_allure_results():
    """Очищение результатов модуля allure-results"""
    allure_dir = Path("allure-results")

    if allure_dir.exists():
        shutil.rmtree(allure_dir)

    allure_dir.mkdir(exist_ok=True)


def to_driver_options(context):

    if context == "local_browser":
        browser.config.base_url = "https://ural-auto.ru/"
        browser.config.timeout = 10
        browser.config.window_width = 1495
        browser.config.window_height = 870

        # Создаем локальный драйвер Chrome
        options = Options()
        driver = webdriver.Chrome(options=options)
        browser.config.driver = driver

    if context == "selenoid":
        # Selenoid
        browser.config.base_url = "https://ural-auto.ru/"
        browser.config.timeout = 10
        browser.config.window_width = 1495
        browser.config.window_height = 870

        # Настройки Selenoid
        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": "128.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True,
            }
        }

        load_dotenv(dotenv_path=utils.file.abs_path_from_project('.env.credentials'))
        options.capabilities.update(selenoid_capabilities)

        # Создаем удаленный драйвер
        driver = webdriver.Remote(
            command_executor=f"https://{os.getenv('SELENOID_LOGIN')}:{os.getenv('SELENOID_PASS')}@{os.getenv('SELENOID_URL')}/wd/hub",
            options=options
        )
        browser.config.driver = driver

    return browser
