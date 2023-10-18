from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url=self.browser.current_url
        assert LoginPageLocators.KEY_LOGIN_URL_WORD in current_url, f"should be {LoginPageLocators.KEY_LOGIN_URL_WORD}, but have {current_url} "

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина

        assert self.is_element_present(*LoginPageLocators.LOGIN_FIELD), "login_field is not provided"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "registration field is not provided"