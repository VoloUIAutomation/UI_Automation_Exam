from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.core import driver
from werkzeug.debug.repr import helper

from Helpers import environment
from Helpers.helpers import GeneralHelpers
from Helpers.test_logger import logger
from selenium.webdriver.common.action_chains import ActionChains

from Pages.header import HeaderPage
from Pages.login import LoginPage
from Pages.result import ResultPage
from TestData import testdata


class TESTHelpers(ResultPage, LoginPage, HeaderPage):
    price_list = None

    def test_1_search(self):
        resultpage = ResultPage(driver)
        headerpage = HeaderPage(driver)
        self.go_to_page(environment.config_data["url"])
        self.change_english()
        headerpage.saerch_data(testdata.search_data)
        self.select_usd_currency()
        resultpage.set_price(testdata.price_min, testdata.price_max)
        self.price_list = resultpage.check_result()
        for price in self.price_list:
            assert 0 <= price <= 50, logger("Result is incorrect", error=True)
        logger("Result is correct!")

        return self

    def change_to_and_click(self):
        self.change_english()
        self.click_myaccount()

    def login_page(self):
        self.login()

    def enter_logo_and_menu_tab(self):
        self.click_on_logo()
        self.click_menu_tab()