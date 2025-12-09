import pytest
from tests.pages.cart_page import CartPage
from tests.pages.catalog_page import CatalogPage

cart_page = CartPage()
catalog_page = CatalogPage()


def test_add_to_cart_product(open_browser_and_accept_cookies):

    catalog_page.go_to_the_catalog_dinamiki()
    (cart_page.add_products_to_cart().assert_count_product_to_cart())
