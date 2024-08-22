import pytest
from selenium import webdriver
from login_page import LoginPage
from admin_page import AdminPage

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestAdminMenu:
    def test_admin_menu(self):
        login_page = LoginPage(self.driver)
        admin_page = AdminPage(self.driver)
        file_path = "data/test_data.xlsx"
        username = "Admin"
        password = "admin123"
        login_page.login(username, password)

        menu_options = [
            "Admin",
            "PIM",
            "Leave",
            "Time",
            "Recruitment",
            "My Info",
            "Performance",
            "Dashboard",
            "Directory",
            "Maintenance",
            "Buzz"
        ]

        for menu in menu_options:
            admin_page.click_menu_option(menu)
