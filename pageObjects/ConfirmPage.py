from __future__ import annotations

from selenium.webdriver.common.by import By

from pageObjects.base_page import BasePage


class ConfirmPage(BasePage):
    country_input = (By.ID, "country")
    purchase_btn = (By.CSS_SELECTOR, "input.btn")
    success_alert = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def search_country(self, country_query: str) -> None:
        field = self.wait_for_visible(self.country_input)
        field.clear()
        field.send_keys(country_query)

    def select_country(self, country_name: str) -> None:
        country_link = (By.LINK_TEXT, country_name)
        self.wait_for_clickable(country_link).click()

    def complete_purchase(self) -> None:
        self.wait_for_clickable(self.purchase_btn).click()

    def get_alert_text(self) -> str:
        return self.wait_for_visible(self.success_alert).text

    @property
    def inputCountry(self):  # noqa: N802
        return self.wait_for_visible(self.country_input)

    @property
    def pol(self):
        return (By.LINK_TEXT, "Poland")

    @property
    def selectPoland(self):  # noqa: N802
        return self.wait_for_clickable((By.LINK_TEXT, "Poland"))

    @property
    def purchaseItem(self):  # noqa: N802
        return self.wait_for_clickable(self.purchase_btn)

    @property
    def successAlert(self):  # noqa: N802
        return self.success_alert

    @property
    def getAlert(self):  # noqa: N802
        return self.wait_for_visible(self.success_alert)
