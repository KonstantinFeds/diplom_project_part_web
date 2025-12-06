from tests.page.cart_page import CartPage

cart_page = CartPage()

def test_add_to_cart_product(accept_cookies,go_to_the_catalog_dinamiki):

    cart_page.add_products_to_cart()
    cart_page.count_product_to_cart_expect()