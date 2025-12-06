import time
from selene import browser,be,command
from tests.page.cart_page import CartPage

cart_page = CartPage()

def test_removing_products_from_the_cart(open_browser,accept_cookies):
    cart_page.add_products_to_cart()
    cart_page

