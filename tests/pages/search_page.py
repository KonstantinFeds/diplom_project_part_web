from selene import browser, have
from tests.pages.locators import Locators


class SearchPage:
    def click_search_string(self):
        browser.element(Locators.SEARCH_BUTTON).click()

        return self

    def insert_name_product(self, value):
        browser.element(Locators.INPUT_SEARCH).type(value).press_enter()

        return self

    def click_on_the_found_product(self):
        browser.element(Locators.SEARCH_RESULT_PRODUCT).click()

        return self

    def assert_name_product(self, value):
        browser.element(Locators.NAME_PRODUCT).should(have.exact_text(value))

        return self
