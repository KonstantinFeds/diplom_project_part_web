from selene import browser, have

from tests.pages.locators import Locators


class CatalogPage:
    def go_to_the_catalog_subwoofer(self):
        browser.element(Locators.CATALOG_BUTTON).click()
        browser.element(Locators.CATALOG_SUBWOOFERS_BUTTON).click()

        return self

    def assert_name_catalog_subwoofer(self, value):
        browser.element(Locators.TITLE_CATALOG_SUBWOOFERS).should(
            have.exact_text(value)
        )

        return self

    def go_to_the_catalog_dinamiki(self):
        browser.element(Locators.CATALOG_BUTTON).click()
        browser.element(Locators.CATALOG_DINAMIKI_BUTTON).click()

        return self

    def assert_products_in_the_catalog(
        self,
        product1,
        product2,
        product3,
        product4,
        product5,
        product6,
        product7,
        product8,
        product9,
    ):
        (
            browser.all(Locators.ALL_PRODUCTS_CATALOG).should(
                have.exact_texts(
                    product1,
                    product2,
                    product3,
                    product4,
                    product5,
                    product6,
                    product7,
                    product8,
                    product9,
                )
            )
        )

        return self

    def checkbox_filter_series_ak_click(self):
        browser.element(Locators.CHECKBOX_SERIES_NAME_AK).click()
        return self

    def checkbox_filter_series_bulava_click(self):
        browser.element(Locators.CHECKBOX_SERIES_NAME_BULAVA).click()
        return self

    def assert_products_with_filter(
        self, product1, product2, product3, product4, product5
    ):
        browser.all(Locators.CATALOG_RESULTS_PRODUCTS).should(
            have.exact_texts(product1, product2, product3, product4, product5)
        )

        return self
