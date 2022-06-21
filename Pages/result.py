from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
import random

result_container = (By.XPATH, "/html/body/div[3]/div[3]/div[2]")
ddl_currency = (By.XPATH, "//*[text()='Currency']//following::div[@class='me']")
usd_price = (By.XPATH, "//div[text()='$ (USD)']")
from_price = (By.ID, "idprice1")
favorite_items = (By.XPATH, "//div[@id='contentr']//a")
to_price = (By.ID, "idprice2")
price_blue_button = (By.ID, "gobtn")

result_price = (By.XPATH, "//div[@id='contentr']//a//div[@class='p']")
contentr_items = (By.XPATH, "//div[@id='contentr']//a")


add_to_favorite = (By.XPATH, "/html/body/div[4]/div[3]/div[2]/div[2]/div")


class ResultPage(GeneralHelpers):

    def select_usd_currency(self):
        self.find_and_click(ddl_currency)
        self.find_and_click(usd_price)
        
    def set_price(self, price_min, price_max):
        self.find_and_send_keys(from_price, price_min)
        self.find_and_send_keys(to_price, price_max)
        self.find_and_click(price_blue_button)
    
    def check_result(self):
        elements = self.find_all(result_price)
        price_list = [el.text for el in elements]
        price_list_number = [int(el.split('$')[1].split(' ')[0]) for el in price_list]
        return price_list_number      

    def add_to_favorites(self):
        n = random.randint(0, 5)
        favorite_items_list = []
        items = self.find_all(contentr_items)
        for i in range(1, n+1):
            items[i].click()
            self.wait_for_page('item')
            self.find_and_click(add_to_favorite)
            item_from_url = self.retrn_url().split("/")[-1]
            favorite_items_list.append(item_from_url)
            self.driver.back()
        return favorite_items_list

    def get_favorite_items(self):
        favorites = self.find_all(favorite_items)
        favorite_list = []
        for favorite in favorites:
            favorite.click()
            self.wait_for_page('item')
            item_from_url = self.retrn_url().split("/")[-1]
            favorite_list.append(item_from_url)
            self.driver.back()
        return favorite_list

