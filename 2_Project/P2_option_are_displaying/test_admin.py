import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from login_page import LoginPage
from admin_page import AdminPage
import openpyxl
from datetime import datetime

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()

def test_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    admin_page = AdminPage(driver)

    # Test data
    username = "Admin"
    password = "admin123"
    tester_name = "Tester"

    # login details
    login_page.login(username, password)

    # Wait for login to complete and the admin page to load
    print("Waiting for the admin menu to be present...")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "menu_admin_viewAdminModule"))
    )
    print("Admin menu is present.")

    # Click on the Admin menu
    admin_page.click_admin_menu()

    # Verify the sub menus
    try:
        admin_page.verify_sub_menus()
        test_result = "Pass"
    except Exception as e:
        print(f"An error occurred: {e}")
        test_result = "Fail"

    # Log test result in Excel
    log_test_result(1, username, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), tester_name, test_result)


def log_test_result(test_id, username, test_time, tester_name, test_result):
    wb = openpyxl.load_workbook("test_data.xlsx")
    ws = wb.active
    ws.append([test_id, username, "Login Test", test_time, tester_name, test_result])
    wb.save("test_data.xlsx")
