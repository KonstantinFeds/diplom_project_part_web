from tests.pages.login_page import LoginPage

login_page = LoginPage()


def test_invalid_login(open_browser_and_accept_cookies):

    (
        login_page.go_to_login_page_click()
        .input_login("TestLogin@mail.ru")
        .input_password("TestPassword")
        .login_button_click()
        .assert_login_error_message("Неверный логин или пароль.")
    )
