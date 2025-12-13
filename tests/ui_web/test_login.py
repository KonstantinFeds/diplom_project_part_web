from tests.pages_ui_web.login_page_ui_web import LoginPage

login_page = LoginPage()


def test_invalid_login(open_site_without_cookies):

    (
        login_page.go_to_login_page_click()
        .input_login("TestLogin@mail.ru")
        .input_password("TestPassword")
        .login_button_click()
        .assert_login_error_message("Неверный логин или пароль.")
    )
