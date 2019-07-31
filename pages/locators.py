from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class ProductPageLocators(object):
    ADD_CARD_LINK = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    GOOD_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    GOOD_NAME_IN_CARD = (By.CSS_SELECTOR, "div#messages > div:nth-child(1) div strong")
    GOOD_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    GOOD_PRICE_IN_CARD = (By.CSS_SELECTOR, "div#messages > div:nth-child(3) div strong")