from pages.product_page import ProductPage
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_cart(browser, link):
def test_guest_can_add_product_to_cart(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
    # открываем страницу
    page.open()
    # проверка кнопки добавить в корзину
    page.check_button_card()
    # выполняем метод добавления товара
    page.add_product_to_card()
    # ответ на вопрос
    page.solve_quiz_and_get_code()
    # проверка товара в корзине
    page.check_product_in_card()
    # проверка цены товара
    page.check_productprice_in_card()

    # time.sleep(200)

# def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
#     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page = ProductPage(browser, link)
#     # открываем страницу
#     page.open()
#     # проверка кнопки добавить в корзину
#     page.check_button_card()
#     # выполняем метод добавления товара
#     page.add_product_to_card()
#     # ответ на вопрос
#     page.solve_quiz_and_get_code()
#     # проверка товара в корзине
#     page.check_product_in_card()
#     # проверка цены товара
#     page.check_productprice_in_card()
#     # проверка что нет успешного сообщения
#     page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
    # открываем страницу
    page.open()
    # проверка что нет успешного сообщения
    page.should_not_be_success_message()

# def test_message_disappeared_after_adding_product_to_cart(browser):
#     # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page = ProductPage(browser, link)
#     # открываем страницу
#     page.open()
#     # проверка кнопки добавить в корзину
#     page.check_button_card()
#     # выполняем метод добавления товара
#     page.add_product_to_card()
#     # ответ на вопрос
#     page.solve_quiz_and_get_code()
#     # проверка товара в корзине
#     page.check_product_in_card()
#     # проверка цены товара
#     page.check_productprice_in_card()
#     # проверка что нет успешного сообщения
#     page.should_be_closed_success_message()
