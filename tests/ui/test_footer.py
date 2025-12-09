
from tests.pages.footer_page import FooterPage

footer_page = FooterPage()


def test_switch_to_german_language(open_browser_and_accept_cookies):
    footer_page.select_german_language()
    footer_page.assert_german_name_catalog_dinamiki(
        "Kopf -\nGerät",
        "Die akustischen\nSysteme",
        "Ein lautes\nGeräusch",
        "Subwoofer",
        "Verstärker",
        "Kopfhörer",
        "Tragbare\nAkustik",
    )
