from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    LOGO = (By.CSS_SELECTOR, ".app_logo")
    CART = (By.ID, "shopping_cart_container")

    def is_displayed(self):
        return self.find_element(self.LOGO).is_displayed()

    def go_to_cart(self):
        self.click(self.CART)