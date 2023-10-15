import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose language")

list_of_languages = ["es", "fr", "en", "ru"]

@pytest.fixture(scope="module")
def browser():
    print("\nstart chrome browser for test..")
    browser_instance = webdriver.Chrome()
    yield browser_instance
    print("\nquit browser..")
    browser_instance.quit()

@pytest.fixture(scope="module")
def language(request):
    chosen_language = request.config.getoption("language")
    if chosen_language not in list_of_languages:
        raise pytest.UsageError(f"--language should be from {list_of_languages}")
    return chosen_language
