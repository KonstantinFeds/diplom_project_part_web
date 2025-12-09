class Locators:
    SEARCH_BUTTON = '[title="Поиск"]'
    INPUT_SEARCH = "#title-search-input"
    SEARCH_RESULT_PRODUCT = 'a.catalog-block__name[href*="molniya-kvark"]'
    NAME_PRODUCT = ".product-detail__name.product-detail__name_mb"

    ADD_TO_CART_BUTTON = (
        ".catalog-block__btn.btn.btn_primary.btn_sm.js-catalog-block__btn"
    )
    CONTINUE_BUYING_BUTTON = ".btn.btn_primary.btn_block.js-modal-close"
    CART_BUTTON = '[id="header_basket_count js-header-cart-click"]'
    SELECT_ALL_PRODUCTS_BUTTON = '[for="cart-select-all"]'
    DELETE_ALL_BUTTON = '[id="cart-delete-all"]'
    EMPTY_CART_TITLE = ".pages-header__title"

    CATALOG_BUTTON = '[title="Каталог"]'
    TITLE_CATALOG_SUBWOOFERS = ".page-header__title"
    CATALOG_SUBWOOFERS_BUTTON = (
        'a.nav-submenu__list-link_title[href="/catalog/subwoofers/"]'
    )
    CATALOG_DINAMIKI_BUTTON = (
        'a.nav-submenu__list-link_title[href="/catalog/dinamiki/"]'
    )
    ALL_PRODUCTS_CATALOG = ".catalog-block__name"

    GERMAN_LANGUAGE_BUTTON = '[title = "Немецкий"]'
    ALL_TITLE_NAME_CATALOG = '[class="catalog-tile__name"]'
