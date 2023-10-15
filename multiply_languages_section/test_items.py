from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_user_click_on_language_button( browser,language):
    browser.get(link)
    form=Select(browser.find_element(By.CLASS_NAME,"form-control"))


    if language=='ru':
        form.select_by_value("ru")
    elif language=='en':
        form.select_by_value("en-gb")
    elif language=='es':
        form.select_by_value("es")
    elif language=='fr':
        form.select_by_value("fr")
    

def test_click_on_change_language_button(browser):
    change=browser.find_element(By.CSS_SELECTOR,"button.btn:nth-child(4)")
    change.click()


def test_user_click_add_button(browser):
    button=WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'button.btn-lg:nth-child(3)')))
   
    button.click()
    

def test_user_see_successfull_message(browser):
    message=browser.find_element(By.CSS_SELECTOR,"div.alert:nth-child(1) > div:nth-child(2)")
    message=message.text
    print(message)
    assert f"Coders at Work" in message,"product not added"
    