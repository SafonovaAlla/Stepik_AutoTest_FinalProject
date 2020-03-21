from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link, 10)
    product_page.open()

    product_page.add_to_basket()

    product_page.should_be_basket_message_equal_to_product_name()
    print("product names are equal in card and message")
    product_page.should_be_basket_message_equal_to_product_price()
    print("product prices are equal in card and message")