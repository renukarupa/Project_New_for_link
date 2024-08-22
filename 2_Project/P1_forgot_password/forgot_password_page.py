from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class ForgotPasswordPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, 'securityAuthentication_userName')
        self.reset_password_button = (By.ID, 'btnSearchValues')
        self.success_message = (By.XPATH, "//div[@id='content']//p[@class='message success']")

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)

    def click_reset_password(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.reset_password_button)
        ).click()

    def is_success_message_displayed(self):
        try:
            success_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.success_message)
            )
            return success_message.is_displayed()
        except TimeoutException:
            return False
