from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_module = (By.XPATH, "//span[text()='PIM']")
        self.employee_list = (By.XPATH, "//a[text()='Employee List']")
        self.search_employee_name_input = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.search_button = (By.XPATH, "//button[text()='Search']")
        self.first_employee_name = (By.XPATH, "(//div[@role='table']//div[@role='row'])[2]//div[@role='cell'][3]")
        self.edit_button = (By.XPATH, "(//div[@role='table']//div[@role='row'])[2]//button[text()='Edit']")
        self.first_name_input = (By.NAME, "firstName")
        self.last_name_input = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[@type='submit']")

    def navigate_to_pim(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.pim_module)
        ).click()

    def click_employee_list(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.employee_list)
        ).click()

    def search_employee(self, name):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.search_employee_name_input)
        ).send_keys(name)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_button)
        ).click()

    def click_first_employee_edit(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.edit_button)
        ).click()

    def edit_employee_details(self, first_name, last_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name_input)
        ).clear()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.first_name_input)
        ).send_keys(first_name)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.last_name_input)
        ).clear()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.last_name_input)
        ).send_keys(last_name)

    def click_save(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.save_button)
        ).click()
