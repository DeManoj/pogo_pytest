from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        browser.maximize_window()
        self.wait = WebDriverWait(browser, 10)  # Explicit wait
        self.actions = ActionChains(browser)
        # self.browser.implicitly_wait(10)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def verify_element_visible(self, by, value, timeout=10):
        try:
            element = self.wait_for_element((by, value), timeout)
            if not element.is_displayed():
                raise AssertionError(f"Element located by {by}='{value}' is not visible.")
        except Exception as e:
            raise AssertionError(f"Failed to find or verify visibility of element: {e}")

    def find(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def click(self, by, value):
        self.find(by, value).click()

    def enter_text(self, by, value, text):
        self.find(by, value).clear()
        self.find(by, value).send_keys(text)


    def press_enter(self, by, value):
        element = self.find(by, value)
        element.send_keys(Keys.ENTER)

    def hover(self, by, value):
        element_to_hover = self.browser.find_element(by, value)
        self.actions.move_to_element(element_to_hover).perform()

    def javascript_click(self, by, value):
        element = self.browser.find_element(by, value)
        self.browser.execute_script("arguments[0].click();", element)

    def select_by_value(self, by, value, option):
        dropdown_element = WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located((by, value))
        )
        self.browser.execute_script("arguments[0].scrollIntoView(true);", dropdown_element)

        select = Select(dropdown_element)
        select.select_by_value(option)
