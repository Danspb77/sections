import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


@pytest.fixture(scope='function')
def browser():
    print("\nstart chrome browser for test..")

    

    browser=webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()