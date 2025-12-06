import time

from selene import browser, be, command


def test_add_to_cart_product(accept_cookies,go_to_the_catalog_dinamiki):

    button_add_to_cart = browser.all('.catalog-block__btn.btn.btn_primary.btn_sm.js-catalog-block__btn')

    for button_cart in button_add_to_cart:
        button_cart.click()
        time.sleep(0.1)
        continue_button = browser.element('.btn.btn_primary.btn_block.js-modal-close')
        continue_button.should(be.clickable)
        continue_button.perform(command.js.scroll_into_view)
        continue_button.click()
