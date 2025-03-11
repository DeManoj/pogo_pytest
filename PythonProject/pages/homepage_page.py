from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    URL = "https://pogo.com/"

    REGISTER_FREE_BUTTON = (By.XPATH, "//div[@class='unauthenticatedSection__1kS-F']//div[contains(text(), 'Register free')]")

    SEARCH_BUTTON = (By.XPATH, "//input[@placeholder='Search for games']")

    SIGN_IN_BUTTON = (By.XPATH, "//div[@class='unauthenticatedSection__1kS-F']//div[contains(text(), 'Sign In')]")

    WHY_REGISTER_LINK = (By.XPATH, "//a[@href='/club-pogo']")

    GET_MORE_PERKS_TOOLTIP_CLOSE_BUTTON = (By.XPATH, "//div[@class='onboardingTooltip__kMqn6 tooltip__2cDLv']//button")

    TOOLTIPS = {
        "why_register": "onboardingTooltip__kMqn6 tooltip__2cDLv",
        "search_games": "onboardingTooltip__kMqn6 tooltip__2lNfp",
        "click_to_preview": "tooltip__2EzsL bottom__36xmD"
    }

    # Generate locators dynamically
    TOOLTIP_LOCATORS = {
        name: (By.XPATH, f"//div[contains(@class, '{css_class}')]")
        for name, css_class in TOOLTIPS.items()
    }

    TOOLTIP_TITLE_LOCATORS = {
        f"{name}_title": (By.XPATH, f"//div[contains(@class, '{css_class}')]//div[@class='title__1l3zf']")
        for name, css_class in TOOLTIPS.items()
    }

    TOOLTIP_DESCRIPTION_LOCATORS = {
        f"{name}_description": (By.XPATH, f"//div[contains(@class, '{css_class}')]//div[@class='copy__R67Vc']")
        for name, css_class in TOOLTIPS.items()
    }

    TOOLTIP_CLOSE_LOCATORS = {
        f"{name}_close": (By.XPATH, f"//div[contains(@class, '{css_class}')]//button")
        for name, css_class in TOOLTIPS.items()
    }

    TOP_GAMES_OF_INDEX = (By.XPATH, "//div[@class='col__1qiUz col-1-1-2-3-3-4-5__2oaS1']")

    def load(self):
        self.browser.get(self.URL)

    def click_register(self):
        self.javascript_click(*self.REGISTER_FREE_BUTTON)

    def click_sign_in_button(self):
        self.javascript_click(*self.SIGN_IN_BUTTON)

    def click_search_for_games(self):
        self.click(*self.SEARCH_BUTTON)

    def enter_text_in_search_for_games(self, games):
        self.enter_text(*self.SEARCH_BUTTON, games)

    def press_enter_in_search_for_games(self):
        self.press_enter(*self.SEARCH_BUTTON)

    def hover_on_search_for_games(self):
        self.hover(*self.SEARCH_BUTTON)

    def hover_on_top_game_by_index(self, index):
        locator = (self.TOP_GAMES_OF_INDEX[0], f"{self.TOP_GAMES_OF_INDEX[1]}[{index}]")
        self.hover(*locator)

    def click_why_register_link(self):
        self.click(*self.WHY_REGISTER_LINK)

    def click_get_more_perks_tooltip_close_button(self):
        self.click(*self.GET_MORE_PERKS_TOOLTIP_CLOSE_BUTTON)

    def get_tooltip_title(self, tooltip_key):
        locator = self.TOOLTIP_TITLE_LOCATORS.get(tooltip_key)
        if locator:
            element = self.wait_for_element(locator)
            return element.text
        else:
            raise ValueError(f"Tooltip title '{tooltip_key}' not found.")

    def get_tooltip_description(self, tooltip_key):
        locator = self.TOOLTIP_DESCRIPTION_LOCATORS.get(tooltip_key)
        if locator:
            element = self.wait_for_element(locator)
            return element.text
        else:
            raise ValueError(f"Tooltip description '{tooltip_key}' not found.")