import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def browser():
    options = Options()
    # options.add_argument("--headless=new")  # Faster headless mode
    options.add_argument("--disable-gpu")  # Disable GPU for stability
    # options.add_argument("--window-size=1920,1080")  # Maximize window
    options.add_argument("--no-sandbox")  # Required for Linux environments
    options.add_argument("--disable-dev-shm-usage")  # Prevent crashes in Docker

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)  # Implicit wait for all elements

    yield driver  # Pass driver to test

    driver.quit()  # Cleanup after test
