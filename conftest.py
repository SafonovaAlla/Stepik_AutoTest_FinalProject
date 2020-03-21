from selenium import webdriver
import pytest

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: es, ru, etc.")


@pytest.fixture(scope="function")
def browser(request):
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()