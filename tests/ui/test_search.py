from selene import browser,have

def test_search_by_product_name(open_browser):
    browser.open('/')
    browser.element('[title="Поиск"]').click()
    browser.element('#title-search-input').type('УРАЛ ЦСП 16 12.80').press_enter()
    browser.element('.catalog-block__desc').click()
    browser.element('.product-detail__name.product-detail__name_mb').should(have.exact_text('УРАЛ ЦСП 16 12.80\n12-канальный усилитель с 16-канальным DSP'))



