from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_card(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_CARD_LINK)
        login_link.click()

    def check_product_in_card(self):
        # получение наименование товара
        el_name_good = self.browser.find_element(*ProductPageLocators.GOOD_NAME)
        name_good = el_name_good.text
        # получение наименования товара в корзине
        el_name_good_card = self.browser.find_element(*ProductPageLocators.GOOD_NAME_IN_CARD)
        name_good_card = el_name_good_card.text
        # проверка наименований
        assert name_good == name_good_card, "Wrong good in card"

    def check_productprice_in_card(self):
        # получение цены товара
        el_price_good = self.browser.find_element(*ProductPageLocators.GOOD_PRICE)
        price_good = el_price_good.text
        # получение цены товара в корзине
        el_price_good_card = self.browser.find_element(*ProductPageLocators.GOOD_PRICE_IN_CARD)
        price_good_card = el_price_good_card.text
        # проверка цен
        assert price_good == price_good_card, "Wrong price good in card"

    def check_button_card(self):
        assert self.is_element_present(*ProductPageLocators.ADD_CARD_LINK), "Button Card is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def should_be_closed_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should be closed"