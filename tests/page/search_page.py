from selene import browser, have


class SearchPage:
    def click_search_string(self):
        browser.element('[title="Поиск"]').click()

        return self

    def insert_name_product(self, value):
        browser.element("#title-search-input").type(value).press_enter()

        return self

    def click_on_the_found_product(self):
        browser.element(".catalog-block__desc").click()

        return self

    def assert_name_product(self, value):
        browser.element(".product-detail__name.product-detail__name_mb").should(
            have.exact_text(value)
        )

        return self
