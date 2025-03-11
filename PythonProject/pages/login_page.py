from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_NEXT_BUTTON = (By.ID, "logInBtn")

    INPUT_FIELDS = {
        "email": (By.ID, "email"),
        "password": (By.ID, "password"),
    }

    LOGGED_IN_USER_AVATAR_IMAGE = (By.XPATH, "//img[@alt='Avatar Image']")

    REMEMBER_ME_CHECKBOX = (By.ID, "rememberMe")

    def enter_text_in_input_fields(self, field_name, text):
        by, value = self.INPUT_FIELDS[field_name]
        self.enter_text(by, value, text)

    def click_login_next_button(self):
        self.click(*self.LOGIN_NEXT_BUTTON)

    def click_basic_info_next_button(self):
        self.click(*self.BASIC_INFO_NEXT_BUTTON)

    def check_remember_me_checkbox(self):
        self.click(*self.REMEMBER_ME_CHECKBOX)

    def click_create_account_button(self):
        self.click(*self.CREATE_ACCOUNT_BUTTON)

    def verify_logged_in_user_avatar_is_visible(self):
        is_visible = self.verify_element_visible(*self.LOGGED_IN_USER_AVATAR_IMAGE)
