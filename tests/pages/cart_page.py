import time
from selene import browser, be, command, have
from tests.pages.locators import Locators


class CartPage:
    def add_products_to_cart(self):

        button_add_to_cart = browser.all(Locators.ADD_TO_CART_BUTTON)

        for button_cart in button_add_to_cart:
            button_cart.click()
            time.sleep(0.5)
            continue_button = browser.element(Locators.CONTINUE_BUYING_BUTTON)
            continue_button.should(be.clickable)
            continue_button.perform(command.js.scroll_into_view)
            continue_button.click()

        return self

    def assert_count_product_to_cart(self):
        cart_count = browser.element(Locators.CART_BUTTON).perform(
            command.js.scroll_into_view
        )

        browser.driver.refresh()
        cart_count.should(have.exact_text("КОРЗИНА\n9"))

        return self

    def cart_button_click(self):
        browser.element(Locators.CART_BUTTON).click()

        return self

    def checkbox_select_all_click(self):
        browser.element(Locators.SELECT_ALL_PRODUCTS_BUTTON).click()

        return self

    def cart_delete_all_button_click(self):
        browser.element(Locators.DELETE_ALL_BUTTON).click()

        return self

    def assert_text_empty_cart(self, value):
        browser.element(Locators.EMPTY_CART_TITLE).should(have.exact_text(value))

        return self
