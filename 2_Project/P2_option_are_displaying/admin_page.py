from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.admin_menu = (By.ID, 'menu_admin_viewAdminModule')
        self.sub_menus = {
            "User Management": (By.ID, 'menu_admin_UserManagement'),
            "Job": (By.ID, 'menu_admin_Job'),
            "Organization": (By.ID, 'menu_admin_Organization'),
            "Qualification": (By.ID, 'menu_admin_Qualifications'),
            "Nationalities": (By.ID, 'menu_admin_nationality'),
            "Corporate Banking": (By.ID, 'menu_admin_corpBanking'),
            "Configuration": (By.ID, 'menu_admin_Configuration')
        }

    def click_admin_menu(self):
        print("Waiting for the admin menu to be clickable...")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.admin_menu)
        ).click()
        print("Admin menu clicked.")

    def verify_sub_menus(self):
        for key, locator in self.sub_menus.items():
            print(f"Waiting for the sub menu {key} to be visible...")
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            print(f"Sub menu {key} is visible.")
