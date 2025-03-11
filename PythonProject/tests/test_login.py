from pages.homepage_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashBoardPage

import time

registered_email = "hfafcdfpddqimbuyyb@hthlm.com"

password = "Pogo@1234"

def test_login_log_out(browser):
    dashboard_page = DashBoardPage(browser)
    homepage_page = HomePage(browser)
    homepage_page.load()

    homepage_page.click_sign_in_button()

    login_page = LoginPage(browser)

    login_page.enter_text_in_input_fields("email", registered_email)

    login_page.click_login_next_button()

    login_page.enter_text_in_input_fields("password", password)

    login_page.click_login_next_button()

    login_page.verify_logged_in_user_avatar_is_visible()

    time.sleep(5)

    dashboard_page.click_user_avatar_image()

    time.sleep(5)

    dashboard_page.click_sign_out_button()

    time.sleep(5)

    dashboard_page.verify_thanks_for_playing_message()

