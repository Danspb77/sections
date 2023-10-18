from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK=(By.CSS_SELECTOR,"#login_link")

class LoginPageLocators():
    # LOGIN_URL ='http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    KEY_LOGIN_URL_WORD='login'
    LOGIN_FIELD= (By.CSS_SELECTOR,"#id_login-username")
    REGISTRATION_EMAIL= (By.CSS_SELECTOR,"#id_registration-email")