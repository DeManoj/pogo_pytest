from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LetsPlayForm(BasePage):
    URL = "https://pogo.com/"

    BIRTH_MONTH_SELECT_FIELD = (By.ID, "birthMonth-autoCompleteInput")
    BIRTH_YEAR_SELECT_FIELD = (By.ID, "birthYear-autoCompleteInput")
    LETSPLAY_BUTTON = (By.XPATH, "//div[text()='let's play!']")

    def load(self):
        self.browser.get(self.URL)

    # def register(self, birthmonth, birthyear):
    #     self.enter_text(*self.BIRTH_MONTH_SELECT_FIELD, birthmonth)
    #     self.enter_text(*self.BIRTH_YEAR_SELECT_FIELD, birthyear)
    #     self.click(*self.LETSPLAY_BUTTON)
    #
    # def is_allowed_to_play(self):
    #     return self.find(*self.DASHBOARD).is_displayed()
    #
    # def is_error_displayed(self):
    #     return "Invalid" in self.find(*self.ERROR_MESSAGE).text
