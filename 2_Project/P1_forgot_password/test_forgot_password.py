import pytest
import openpyxl
from selenium import webdriver
from login_page import LoginPage
from forgot_password_page import ForgotPasswordPage

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def get_test_data():
    workbook = openpyxl.load_workbook("test_data.xlsx")
    sheet = workbook.active
    test_data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        test_data.append(row)
    return test_data

@pytest.mark.parametrize("test_id, username, expected_result", get_test_data())
def test_forgot_password(setup, test_id, username, expected_result):
    driver = setup
    login_page = LoginPage(driver)
    forgot_password_page = ForgotPasswordPage(driver)

    # Load the login page
    login_page.load()

    # Click on 'Forgot your password?' link
    login_page.click_forgot_password()

    # Enter username and reset password
    forgot_password_page.enter_username(username)
    forgot_password_page.click_reset_password()

    # Verify success message
    assert forgot_password_page.is_success_message_displayed() == expected_result, f"Test failed for username '{username}'"
