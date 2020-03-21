from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini span.btn-group > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_INPUT_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_INPUT_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#register_form button")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "form#add_to_basket_form button.btn-add-to-basket")
    PRODUCT_NAME_PRODUCT = (By.CSS_SELECTOR, "article.product_page div.product_main h1")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "article.product_page div.product_main p.price_color")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert-success")


class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_MESSAGE_PARAGRAPH = (By.CSS_SELECTOR, "#content_inner > p")