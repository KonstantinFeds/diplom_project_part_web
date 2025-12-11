from selene import browser, have
from tests.pages.search_page import SearchPage

search_page = SearchPage()


def test_search_by_product_name(open_site_without_cookies):

    (
        search_page.click_search_string()
        .insert_name_product("УРАЛ")
        .click_on_the_found_product()
        .assert_name_product("УРАЛ МОЛНИЯ КВАРК\nПортативная акустическая система")
    )
