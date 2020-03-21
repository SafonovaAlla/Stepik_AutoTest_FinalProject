from selenium import webdriver
import pytest

def pytest_addoption(parser):
    boo = 'moo'


@pytest.fixture(scope="function")
def browser(request):
    options = webdriver.ChromeOptions()
    options.add_argument('lang=en')
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_GB'})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()