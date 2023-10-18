from selenium.webdriver.common.by import By


class BasketPageLocators():
    
    BUTTON= (By.CSS_SELECTOR,"button.btn-lg:nth-child(3)")
    PRODUCT_NAME= (By.CSS_SELECTOR,"div.product_main h1")
    SUCCESSFUL_MESSAGE=(By.CSS_SELECTOR,"div.alertinner")

    BASKET_TOTAL=(By.CSS_SELECTOR,"div.alert:nth-child(3) > div:nth-child(2) > p:nth-child(1)")

    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
