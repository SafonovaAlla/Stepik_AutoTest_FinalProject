import pytest
from .pages.product_page import ProductPage
import time

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    print("will test link [{}]".format(link))
    product_page = ProductPage(browser, link, 10)
    product_page.open()

    product_page.add_to_basket()

    product_page.should_be_basket_message_equal_to_product_name()
    print("product names are equal in card and message")
    product_page.should_be_basket_message_equal_to_product_price()
    print("product prices are equal in card and message")

    print("test link [{}] done".format(link))


@pytest.mark.xfail
@pytest.mark.negative
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    # Открываем страницу товара
    product_page = ProductPage(browser, link, 10)
    product_page.open()
    # Добавляем товар в корзину
    product_page.add_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page.should_not_be_success_message()


@pytest.mark.negative
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"])
def test_guest_cant_see_success_message(browser, link):
    # Открываем страницу товара
    product_page = ProductPage(browser, link, 10)
    product_page.open()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    product_page.should_not_be_success_message()


@pytest.mark.xfail
@pytest.mark.negative
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    # Открываем страницу товара
    product_page = ProductPage(browser, link, 10)
    product_page.open()
    # Добавляем товар в корзину
    product_page.add_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    product_page.should_success_message_disappeared()