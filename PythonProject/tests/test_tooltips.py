import pytest
from selenium.webdriver.common.by import By

from pages.homepage_page import HomePage

import time


def test_tooltips(browser):
    homepage_page = HomePage(browser)
    homepage_page.load()

    homepage_page.hover_on_search_for_games()

    search_for_games_tooltip_title = homepage_page.get_tooltip_title("search_games_title")

    assert search_for_games_tooltip_title == "Search for More"

    search_for_games_tooltip_description = homepage_page.get_tooltip_description("search_games_description")

    assert search_for_games_tooltip_description == "Search For Games By Title Or Category, Such As \"Mahjong\" Or \"Solitaire.\""

    time.sleep(5)

    homepage_page.hover_on_top_game_by_index(3)

    time.sleep(5)

    click_to_preview_tooltip_title = homepage_page.get_tooltip_title("click_to_preview_title")

    assert click_to_preview_tooltip_title == "Click to Preview"

    time.sleep(5)

    # why_register_tooltip_title = homepage_page.get_tooltip_title("why_register_title")
    #
    # assert why_register_tooltip_title == "Get More Perks"



