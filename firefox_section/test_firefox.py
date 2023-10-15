from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest
import selenium



link = "http://google.com"



def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element(By.TAG_NAME, "textarea")
    

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")