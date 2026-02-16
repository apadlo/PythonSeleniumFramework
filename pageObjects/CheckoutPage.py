from __future__ import annotations

import re

from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.base_page import BasePage


class CheckoutPage(BasePage):
    product_cards = (By.CSS_SELECTOR, ".card")
    product_titles = (By.CSS_SELECTOR, ".card-title a")
    cart_counter = (By.CSS_SELECTOR, "a.nav-link.btn.btn-primary")
    btn_checkout = (By.CSS_SELECTOR, "button.btn.btn-success")

    def add_product_to_cart(self, product_name: str) -> None:
        add_button = (
            By.XPATH,
            f"//a[text()='{product_name}']/ancestor::div[contains(@class,'card')]//button",
        )
        self.wait_for_clickable(add_button).click()

    def get_product_titles(self) -> list[str]:
        return [el.text.strip() for el in self.wait_for_all_visible(self.product_titles)]

    def get_cart_count(self) -> int:
        text = self.wait_for_visible(self.cart_counter).text
        # Handles values like "Checkout (1)" and labels that include hidden "(current)" text.
        match = re.search(r"\((\d+)\)", text)
        if match:
            return int(match.group(1))
        fallback = re.search(r"\d+", text)
        return int(fallback.group(0)) if fallback else 0

    def open_cart(self) -> None:
        self.wait_for_clickable(self.cart_counter).click()

    def proceed_to_checkout(self) -> ConfirmPage:
        self.wait_for_clickable(self.btn_checkout).click()
        return ConfirmPage(self.driver)

    @property
    def addBlackberry(self):  # noqa: N802
        return self.wait_for_clickable((By.XPATH, "//a[text()='Blackberry']/../../../div[2]/button"))

    @property
    def gotoBasket(self):  # noqa: N802
        return self.wait_for_clickable(self.cart_counter)

    def gotoCheckout(self):  # noqa: N802
        return self.proceed_to_checkout()
