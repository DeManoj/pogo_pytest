from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegistrationPage(BasePage):

    DROPDOWN_FIELDS = {
        "country": (By.ID, "clientreg_country-selctrl"),
        "month": (By.ID, "clientreg_dobmonth-selctrl"),
        "day": (By.ID, "clientreg_dobday-selctrl"),
        "year": (By.ID, "clientreg_dobyear-selctrl"),
        "profile_visibility": (By.ID, "friend_visibility_selctrl")
    }

    OPTIONS = {
        "country": "NP",
        "month": "7",
        "day": "17",
        "year": "2000",
        "visible_to": "EVERYONE"
    }

    DOB_NEXT_BUTTON = (By.ID, "countryDobNextBtn")

    INPUT_FIELDS = {
        "email": (By.ID, "email"),
        "ea_id": (By.ID, "originId"),
        "password": (By.ID, "password"),
    }

    BASIC_INFO_NEXT_BUTTON = (By.ID, "basicInfoNextBtn")

    CREATE_ACCOUNT_BUTTON = (By.ID, "submitBtn")

    CHECKBOXES = {
        "email_visibility": (By.ID, "emailVisibility"),
        "contact_me": (By.ID, "contactMe"),
        "read_accept": (By.ID, "readAccept")
    }

    def enter_text_in_input_fields(self, field_name, text):
        by, value = self.INPUT_FIELDS[field_name]  # Unpack locator
        self.enter_text(by, value, text)  # Call BasePage method

    def fill_inputs(self, data):
        for field, text in data.items():
            self.enter_text(field, text)

    def click_dropdown(self, field_name):
        self.click(*self.DROPDOWN_FIELDS[field_name])

    def select_option(self, field_name):
        by, value = self.DROPDOWN_FIELDS[field_name]
        option_value = self.OPTIONS[field_name]
        self.select_by_value(by, value, option_value)

    def click_dob_next_button(self):
        self.click(*self.DOB_NEXT_BUTTON)

    def click_basic_info_next_button(self):
        self.click(*self.BASIC_INFO_NEXT_BUTTON)

    def check_checkbox(self, check_box_name):
        self.click(*self.CHECKBOXES)

    def click_create_account_button(self):
        self.click(*self.CREATE_ACCOUNT_BUTTON)