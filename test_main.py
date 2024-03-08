import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def browser():
    # Set up the Selenium WebDriver
    driver = webdriver.Chrome()
    yield driver
    # Teardown - close the browser after the tests
    driver.quit()

def test_title_displayed(browser):
    # Open the application
    browser.get("http://192.168.0.104:8501")

    # Check if the title is displayed
    expected_title = "Про-классифицируй текст"
    actual_title = browser.title

    # Check if the actual title matches the expected title
    assert actual_title == expected_title, "Test Failed: Title is not displayed correctly."
