from selenium.webdriver.common.by import By
from Helpers.test_logger import logger

email_field = (By.ID, "_idyour_email")
pass_field = (By.ID, "_idpassword")
btn_login = (By.ID, "action__form_action0")
lbl_account = (By.XPATH, "//*[@id='ma']")

from Helpers.helpers import GeneralHelpers
from Helpers.environment import config_data

class LoginPage(GeneralHelpers):

    def login(self):
        self.find_and_send_keys(email_field, config_data["email"])
        self.find_and_send_keys(pass_field, config_data["password"])
        self.find_and_click(btn_login)
        self.wait_for_page('my')
        logger(f"User successfully is logged to the system.")

    def click_myaccount(self):
        self.find_and_click(lbl_account)
        self.wait_for_page('login')