from pages.homepage_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashBoardPage
import time
from pages.search_result_page import SearchResultPage

game_to_search = "solitaire"

registered_email = "hfafcdfpddqimbuyyb@hthlm.com"

password = "Pogo@1234"

def test_search_game(browser):
    dashboard_page = DashBoardPage(browser)
    search_result_page = SearchResultPage(browser)
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

    homepage_page.click_search_for_games()

    time.sleep(5)

    homepage_page.enter_text_in_search_for_games(game_to_search)

    homepage_page.press_enter_in_search_for_games()

    search_result_page.click_on_game_of_index(1)

    time.sleep(5)

    search_result_page.verify_game_detail_section_is_visible()

    search_result_page.verify_play_now_button_is_visible_inside_game_detail_section()

    time.sleep(5)

    dashboard_page.click_user_avatar_image()

    time.sleep(5)

    dashboard_page.click_sign_out_button()

    time.sleep(5)

    dashboard_page.verify_thanks_for_playing_message()

    time.sleep(5)