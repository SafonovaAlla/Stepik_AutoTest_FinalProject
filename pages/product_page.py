from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
        self.solve_quiz_and_get_code()

    def should_be_basket_message_equal_to_product_name(self):
        assert self.is_elements_text_equal(ProductPageLocators.PRODUCT_NAME_PRODUCT, ProductPageLocators.PRODUCT_NAME_MESSAGE), \
            "Can not detect equality of the good name in card and basket message"

    def should_be_basket_message_equal_to_product_price(self):
        assert self.is_elements_text_equal(ProductPageLocators.PRICE_PRODUCT, ProductPageLocators.PRICE_MESSAGE), \
            "Can not detect equality of the good price in card and basket message"
