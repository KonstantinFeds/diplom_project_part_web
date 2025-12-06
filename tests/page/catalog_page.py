from selene import browser, have


class CatalogPage:
    def go_to_the_catalog_subwoofer(self):
        browser.element('[title="Каталог"]').click()
        browser.element('a.nav-submenu__list-link_title[href="/catalog/subwoofers/"]').click()

    def expected_products_in_the_catalog(self,product1,product2,product3,product4,product5,product6,product7,product8,product9):
        (browser.all('.catalog-block__name')
         .should(have.exact_texts(product1,product2,product3,product4,product5,product6,product7,product8,product9)))


