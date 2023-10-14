from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest
import selenium

def calculate_answer():
    return math.log(int(time.time()))

link="https://stepik.org/lesson/236895/step/1"

stepik_lessons = [
    # "https://stepik.org/lesson/236895/step/1",
    # "https://stepik.org/lesson/236896/step/1"
    # "https://stepik.org/lesson/236897/step/1",
    # "https://stepik.org/lesson/236898/step/1",
    # "https://stepik.org/lesson/236899/step/1",
    # "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
]



@pytest.mark.parametrize("link1",stepik_lessons)
class Test_login():
    
    def test_put_loggin_and_password(self,browser,link1):
        
        browser.get(link1)
        browser.implicitly_wait(10)
        loggin = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.ID, "ember35")))
        loggin=browser.find_element(By.ID,"ember35")
        loggin.click()

        email=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.ID,"id_login_email")))
        email.send_keys("dan.shell@bk.ru")
        password=browser.find_element(By.ID,"id_login_password")
        password.send_keys("first@27")

        button=browser.find_element(By.XPATH,'//button[text()="Войти"]')
        button.click()
        time.sleep(7)


    # @pytest.mark.xfail(reason="not enteractable element")

    # def test_give_answer(self,browser,link1):
        WebDriverWait(browser, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")

        field=browser.find_element(By.TAG_NAME,"textarea")
        if field.is_enabled():
            print("Element is enabled.")
        field.click()
        # field = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.ID, "ember101")))
        answer=calculate_answer()
        
        field.send_keys(answer)

        submit=WebDriverWait(browser,20).until(EC.element_to_be_clickable((By.CLASS_NAME,'submit-submission')))
        
        submit.click()

        
        
        # approving=WebDriverWait(browser,10).until(EC.presence_of_element_located((By.CLASS_NAME,"smart-hint")))
        
        # approving=approving.text()

        # assert "Correct!"==approving,"wrong test"
        
        

    
