from selene import browser


class SearchPage:
    def click_search_string(self):
        browser.element('[title="Поиск"]').click()

    def insert_name_product(self,value):
        browser.element('#title-search-input').type(value).press_enter()
