import time
from selene import browser, be, command
from tests.pages.cart_page import CartPage
from tests.pages.catalog_page import CatalogPage

cart_page = CartPage()
catalog_page = CatalogPage()


def test_removing_products_from_the_cart(open_site_without_cookies):

    catalog_page.go_to_the_catalog_dinamiki()
    (
        cart_page.add_products_to_cart()
        .cart_button_click()
        .checkbox_select_all_click()
        .cart_delete_all_button_click()
        .assert_text_empty_cart("В КОРЗИНЕ ПУСТО,")
    )
