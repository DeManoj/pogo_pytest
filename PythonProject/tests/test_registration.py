import pytest
from selenium.webdriver.common.by import By

from pages.homepage_page import HomePage
from pages.registration_page import RegistrationPage

from utils.helpers import generate_random_string

import time

email = generate_random_string(6) + "@outlook.com"

ea_id = generate_random_string(12)

def test_registration(browser):
    homepage_page = HomePage(browser)
    homepage_page.load()

    homepage_page.click_register()

    registration_page = RegistrationPage(browser)

    registration_page.click_dropdown("country")

    registration_page.select_option("country")

    registration_page.click_dropdown("month")

    registration_page.select_option("month")

    registration_page.click_dropdown("day")

    registration_page.select_option("day")

    registration_page.click_dropdown("year")

    registration_page.select_option("year")

    registration_page.click_dob_next_button()

    time.sleep(5)

    registration_page.enter_text_in_input_fields("email", email)

    registration_page.enter_text_in_input_fields("ea_id", ea_id)

    registration_page.enter_text_in_input_fields("password", "Pogo@123#")

    registration_page.click_basic_info_next_button()

    time.sleep(5)

    registration_page.click_dropdown("profile_visibility")

    registration_page.select_option("visible_to")

    registration_page.check_checkbox("email_visibility")

    registration_page.check_checkbox("contact_me")

    registration_page.check_checkbox("read_accept")

    registration_page.click_create_account_button()

    time.sleep(5)

