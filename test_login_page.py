from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_guest_can_login_or_register(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()  # сразу три проверки, подтверждающте, что мы на странице "войти или зарегистрироваться"