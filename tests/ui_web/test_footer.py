from tests.pages_ui_web.footer_page_ui_web import FooterPage

footer_page = FooterPage()


def test_switch_to_german_language(open_site_without_cookies):
    (
        footer_page.select_german_language().assert_german_name_catalog(
            "Kopf -\nGerät",
            "Die akustischen\nSysteme",
            "Ein lautes\nGeräusch",
            "Subwoofer",
            "Verstärker",
            "Kopfhörer",
            "Tragbare\nAkustik",
        )
    )
