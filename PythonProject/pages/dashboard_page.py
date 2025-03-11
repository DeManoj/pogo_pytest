from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashBoardPage(BasePage):
    LOGGED_IN_USER_AVATAR_IMAGE = (By.XPATH, "//img[@alt='Avatar Image']")

    SIGN_OUT_BUTTON = (By.XPATH, "//div[text()='Sign Out']")

    THANKS_FOR_PLAYING_MESSAGE = (By.XPATH, "//h1[text()='Thanks for Playing!']")

    def click_user_avatar_image(self):
        self.click(*self.LOGGED_IN_USER_AVATAR_IMAGE)

    def click_sign_out_button(self):
        self.javascript_click(*self.SIGN_OUT_BUTTON)

    def verify_thanks_for_playing_message(self):
        self.verify_element_visible(*self.THANKS_FOR_PLAYING_MESSAGE)