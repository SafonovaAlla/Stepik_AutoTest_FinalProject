from selenium import webdriver
import pytest
from datetime import datetime

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        opts = webdriver.ChromeOptions()
        opts.add_argument('lang=en')
        opts.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_GB'})
        browser = webdriver.Chrome(options=opts)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        from selenium.webdriver import Firefox
        from selenium.webdriver.firefox.options import Options
        opts = Options()
        opts.add_argument('lang=en')
        browser = webdriver.Firefox(options=opts)
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    print("\nquit browser..")
    # получаем переменную с текущей датой и временем в формате ГГГГ-ММ-ДД_ЧЧ-ММ-СС
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # делаем скриншот с помощью команды Selenium'а и сохраняем его с именем "screenshot-ГГГГ-ММ-ДД_ЧЧ-ММ-СС"
    browser.save_screenshot('screenshot-%s.png' % now)
    browser.quit()
