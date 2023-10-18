from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from .pages.product_page import BasketPage
import time
def test_guest_can_add_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page=BasketPage(browser, link)
    page.open()
    page.click_on_add_to_busket_button()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.compare_product_cost_and_total_basket()
    # time.sleep(20)

