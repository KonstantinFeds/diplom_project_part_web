import pytest
from tests.pages_ui_web.cart_page_ui_web import CartPage
from tests.pages_ui_web.catalog_page_ui_web import CatalogPage

cart_page = CartPage()
catalog_page = CatalogPage()


def test_add_to_cart_product(open_site_without_cookies):

    catalog_page.go_to_the_catalog_dinamiki()
    (cart_page.add_products_to_cart().assert_count_product_to_cart())
