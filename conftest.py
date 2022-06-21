import pytest
from selenium import webdriver
import logging

@pytest.fixture
def driver():
    driver = webdriver.Chrome(executable_path='D:/Finala_Project_06-22/chromedriver.exe')
    yield driver
    driver.quit()





@pytest.fixture
def logger(msg="", error=False):
    if error:
        logging.error(msg)
    else:
        logging.info(msg)
