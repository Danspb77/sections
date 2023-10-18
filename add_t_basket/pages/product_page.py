
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def click_on_add_to_busket_button(self):
        button=self.browser.find_element(*BasketPageLocators.BUTTON)
        
        button.click()
    def should_be_button_toa_add_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BUTTON), "Button isn't presented"

    def should_be_message_about_adding(self):
        assert self.browser.find_element(*BasketPageLocators.SUCCESSFUL_MESSAGE), "message about successful adding isn't provided"

        successful_message=self.browser.find_element(*BasketPageLocators.SUCCESSFUL_MESSAGE).text

        product_name=self.browser.find_element(*BasketPageLocators.PRODUCT_NAME).text

        assert product_name in successful_message, "Successful massage isn't provided"

    def compare_product_cost_and_total_basket(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_TOTAL), "message about successful basket total"

        assert self.browser.find_element(*BasketPageLocators.PRODUCT_PRICE), "message about product_price"

        basket_total=self.browser.find_element(*BasketPageLocators.BASKET_TOTAL).text

        product_price=self.browser.find_element(*BasketPageLocators.PRODUCT_PRICE).text

        assert product_price in basket_total, "Successful compare of prices isn't provided"





