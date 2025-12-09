from selene import browser, have


class CatalogPage:
    def go_to_the_catalog_subwoofer(self):
        browser.element('[title="Каталог"]').click()
        browser.element(
            'a.nav-submenu__list-link_title[href="/catalog/subwoofers/"]'
        ).click()

        return self

    def assert_name_catalog_subwoofer(self, value):
        browser.element(".page-header__title").should(have.exact_text(value))

        return self

    def go_to_the_catalog_dinamiki(self):
        browser.element('[title="Каталог"]').click()
        browser.element(
            'a.nav-submenu__list-link_title[href="/catalog/dinamiki/"]'
        ).click()

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
            browser.all(".catalog-block__name").should(
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
