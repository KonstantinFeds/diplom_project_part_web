from selene import browser,have
from tests.page.search_page import SearchPage

search_page = SearchPage()

def test_search_by_product_name(open_browser,accept_cookies):

    search_page.click_search_string()
    search_page.insert_name_product('УРАЛ ЦСП 16 12.80')
    search_page.click_on_the_found_product()
    search_page.assert_name_product('УРАЛ ЦСП 16 12.80\n12-канальный усилитель с 16-канальным DSP')


