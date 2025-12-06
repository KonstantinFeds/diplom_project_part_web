import pytest
from selene import browser,have



def test_go_to_the_catalog_subwoofer(open_browser):
    browser.open('/')
    browser.element('[title="Каталог"]').click()
    browser.element('a.nav-submenu__list-link_title[href="/catalog/subwoofers/"]').click()
    browser.element('.page-header__title').should(have.exact_text('САБВУФЕРЫ'))
    (browser.all('.catalog-block__name')
     .should(have.exact_texts('ТТ 12',
                             'МОЛОТ 12','ТТ 15',
                             'ПМН-1 "Черная Вдова"',
                             'МОЛОТ 10',
                             'СИМФОНИЯ 15',
                             'УЛЬТИМАТУМ 12',
                             'УЛЬТИМАТУМ 15',
                             'ПАТРИОТ 6,5')))
