from selenium.webdriver.common.by import By
from Helpers.helpers import GeneralHelpers
import time
favorite_ads = (By.XPATH, "//div[text()='Favorite Ads']")
my_account_icon = (By.XPATH, '//*[@id="ma"]')



class Favorite(GeneralHelpers):
    favorite_items = (By.XPATH, "//div[@id='contentr']//a")
    favorite_items_remove = (By.XPATH, '//div[@original-title="Remove from favorites"]')

    def check_favorite_ads(self):
        self.hover_elem(self.find(my_account_icon))
        time.sleep(2)
        self.find_and_click(favorite_ads)

    def clear_favorites(self):
        f_items = self.find_all(self.favorite_items_remove)
        if f_items:
            for f_item in f_items:
                time.sleep(0.5)
                f_item.click()
