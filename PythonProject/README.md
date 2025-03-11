# pogo_pytest
Automation script to test the https://www.pogo.com for features like, login, registration, search games and tooltips

Prerequisites
Make sure you have Python 3.x installed on your system.

Setup Instructions
1. Clone the repository:
    git clone https://github.com/DeManoj/pogo_pytest
    cd repository-name
2. Install dependencies:
    You can install all the necessary Python dependencies by running:
    pip install -r requirements.txt
3. Configure WebDriver:
    Ensure you have a compatible ChromeDriver or other WebDriver for your browser.
4. Run tests:
    To run all the tests, simply use:
    pytest
    Or to run specific tests:
    pytest tests/test_login.py
5. Running the Tests with HTML Reports:
    You can run the tests and generate an HTML report by using the following command:
    pytest --html=reports/test_report.html 
    This will generate a detailed test execution report in the root folder.


Files Overview

1.  tests/: Contains the test case files for different functionalities.
2. pages/: Contains Page Object Model (POM) files that handle page elements and actions.
3. utils/: Contains utility functions like configuration and helper functions.
4. conftest.py: Contains global pytest fixtures for setting up browser configurations.
5. pytest.ini: Pytest configuration for test settings.







