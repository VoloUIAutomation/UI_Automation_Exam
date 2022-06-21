from Helpers.helpers import GeneralHelpers
from Pages.header import HeaderPage
from Pages.result import ResultPage
from Helpers import environment
from Helpers.test_logger import logger
from TestData import testdata
from Tests.some_helpers import TESTHelpers

"""
1. Navigate to lits.am
2. Search by "house" word
3. Filter by Currency with USD and Price with 0-50 $
4. Click on blue icon
5. Check that result's prices are in filtered range
"""


def test_search(driver):
    result = TESTHelpers(driver)
    result.test_1_search()
    






