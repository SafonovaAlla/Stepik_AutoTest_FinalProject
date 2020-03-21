from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "form#add_to_basket_form button.btn-add-to-basket")
    PRODUCT_NAME_PRODUCT = (By.CSS_SELECTOR, "article.product_page div.product_main h1")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "article.product_page div.product_main p.price_color")
    PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) strong")