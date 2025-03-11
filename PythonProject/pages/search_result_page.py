from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultPage(BasePage):
    GAME_OF_INDEX = (By.XPATH, "//div[@class='gameTile__3amEb hoverAnimation__2bJt5']")

    GAME_DETAIL_SECTION = (By.XPATH, "//div[@class='bladeDetail__3aH5o free__2q3jy']")

    PLAY_NOW_BUTTON = (By.XPATH, "//button[@class='default__1rbFd primary__3GVte button__3Z-Ug playButton__1NRst']")

    def click_on_game_of_index(self, index):
        locator = (self.GAME_OF_INDEX[0], f"{self.GAME_OF_INDEX[1]}[{index}]")
        self.click(*locator)

    def verify_game_detail_section_is_visible(self):
        self.verify_element_visible(*self.GAME_DETAIL_SECTION)

    def verify_play_now_button_is_visible_inside_game_detail_section(self):
        self.verify_element_visible(*self.PLAY_NOW_BUTTON)