import time

from Helpers.helpers import GeneralHelpers
from Pages.header import HeaderPage
from Pages.login import LoginPage
from Helpers import environment
from Pages.result import ResultPage
from Pages.favorite import Favorite
from Tests.some_helpers import TESTHelpers

"""

1. Login to the system
2. Go to Electronics page
3. Add random number of products as a favorite
4. Go to My Account-> Favorite Ads
5. Check that Favorite page contains correct(selected) products

"""

def test_favorite(driver):
    helper = GeneralHelpers(driver)
    headerpage = HeaderPage(driver)
    resultpage = ResultPage(driver)
    test_helper = TESTHelpers(driver)
    loginpage = LoginPage(driver)
    favoritepage = Favorite(driver)

    helper.go_to_page("https://www.list.am/")
    test_helper.change_to_and_click()
    test_helper.login()
    headerpage.click_on_logo()
    time.sleep(5)
    favoritepage.check_favorite_ads()
    time.sleep(5)
    favoritepage.clear_favorites()
    # headerpage.click_on_logo()
    # headerpage.click_menu_tab()
    test_helper.enter_logo_and_menu_tab()
    time.sleep(5)
    favorite_item = resultpage.add_to_favorites()
    favoritepage.check_favorite_ads()
    my_favorite_list = resultpage.get_favorite_items()
    assert sorted(favorite_item) == sorted(my_favorite_list)



