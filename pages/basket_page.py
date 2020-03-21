from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "Basket items are presented, but should not be"


    def should_be_empty_basket_message(self):
        element = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE_PARAGRAPH)
        element_text = element.text
        assert "basket is empty" in element_text, "Can not find empty basket message"
