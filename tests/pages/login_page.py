from selene import browser, have

from tests.pages.locators import Locators


class LoginPage:

    def go_to_login_page_click(self):
        browser.element(Locators.LOGIN_PAGE_BUTTON).click()
        return self

    def input_login(self, value):
        browser.element(Locators.INPUT_USER_LOGIN).type(value)

        return self

    def input_password(self, value):
        browser.element(Locators.INPUT_USER_PASSWORD).type(value)
        return self

    def login_button_click(self):
        browser.element(Locators.LOGIN_BUTTON).click()
        return self

    def assert_login_error_message(self, value):
        browser.element(Locators.LOGIN_ERROR_MESSAGE).should(have.exact_text(value))
