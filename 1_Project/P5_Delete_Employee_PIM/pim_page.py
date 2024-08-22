from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_module = (By.XPATH, "//span[text()='PIM']")
        self.employee_list_button = (By.XPATH, "//a[text()='Employee List']")
        self.first_employee_checkbox = (By.XPATH, "//tbody/tr[1]/td[1]/input")
        self.delete_button = (By.XPATH, "//button[text()='Delete']")
        self.confirm_delete_button = (By.XPATH, "//button[text()='Ok']")

    def navigate_to_pim(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.pim_module)
        ).click()

    def click_employee_list(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.employee_list_button)
        ).click()

    def delete_first_employee(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.first_employee_checkbox)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.delete_button)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.confirm_delete_button)
        ).click()
