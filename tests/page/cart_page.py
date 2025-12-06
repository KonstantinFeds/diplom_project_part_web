import time
from selene import browser, be, command, have


class CartPage:
    def add_products_to_cart(self):

        button_add_to_cart = browser.all('.catalog-block__btn.btn.btn_primary.btn_sm.js-catalog-block__btn')

        for button_cart in button_add_to_cart:
            button_cart.click()
            time.sleep(0.5)
            continue_button = browser.element('.btn.btn_primary.btn_block.js-modal-close')
            continue_button.should(be.clickable)
            continue_button.perform(command.js.scroll_into_view)
            continue_button.click()


    def assert_count_product_to_cart(self):
        cart_count = browser.element("[id='header_basket_count js-header-cart-click']").perform(
            command.js.scroll_into_view)

        browser.driver.refresh()
        cart_count.should(have.exact_text('КОРЗИНА\n9'))

