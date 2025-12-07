from selene import browser, have
from tests.page.search_page import SearchPage

search_page = SearchPage()


def test_search_by_product_name(open_browser_and_accept_cookies):

    (
        search_page.click_search_string()
        .insert_name_product("УРАЛ ЦСП 16 12.80")
        .click_on_the_found_product()
        .assert_name_product(
            "УРАЛ ЦСП 16 12.80\n12-канальный усилитель с 16-канальным DSP"
        )
    )
