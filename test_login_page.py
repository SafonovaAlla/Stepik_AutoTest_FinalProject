from .pages.base_page import BasePage
from .pages.login_page import LoginPage

def test_guest_can_login_or_register(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_login_page()  # сразу три проверки, подтверждающте, что мы на странице "войти или зарегистрироваться"