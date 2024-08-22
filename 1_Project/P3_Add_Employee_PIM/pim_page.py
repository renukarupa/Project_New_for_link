from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_module = (By.XPATH, "//span[text()='PIM']")
        self.add_employee_button = (By.XPATH, "//button[text()='Add']")
        self.first_name_input = (By.NAME, "firstName")
        self.first_name_input = (By.NAME, "middleName")
        self.last_name_input = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[@type='submit']")

    def navigate_to_pim(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.pim_module)
        ).click()

    def click_add_employee(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_employee_button)
        ).click()

    def enter_employee_details(self, first_name,middle_name,last_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name_input)
        ).send_keys(first_name)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.middle_name_input)
        ).send_keys(middle_name)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.last_name_input)
        ).send_keys(last_name)

    def click_save(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.save_button)
        ).click()
