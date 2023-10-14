import pytest
import selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser_instance = webdriver.Chrome()
    browser_instance.execute_script("""
    var css = document.createElement("style");
    css.type = "text/css";
    css.innerHTML = "* { transition: none !important; animation: none !important; }";
    document.head.appendChild(css);
""")

    yield browser_instance 
    print("\nquit browser..")
    browser_instance.quit()
