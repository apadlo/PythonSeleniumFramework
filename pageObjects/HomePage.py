from __future__ import annotations

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.base_page import BasePage


class HomePage(BasePage):
    shop = (By.LINK_TEXT, "Shop")
    name_input = (By.CSS_SELECTOR, "input[name='name']")
    email_input = (By.NAME, "email")
    icecream_checkbox = (By.ID, "exampleCheck1")
    gender_dropdown = (By.ID, "exampleFormControlSelect1")
    submit_button = (By.XPATH, "//input[@type='submit']")
    success_info = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def open_shop(self) -> CheckoutPage:
        self.wait_for_clickable(self.shop).click()
        return CheckoutPage(self.driver)

    # Backward-compatible alias
    def shopItems(self) -> CheckoutPage:  # noqa: N802
        return self.open_shop()

    def fill_name(self, value: str) -> None:
        field = self.wait_for_visible(self.name_input)
        field.clear()
        field.send_keys(value)

    def fill_email(self, value: str) -> None:
        field = self.wait_for_visible(self.email_input)
        field.clear()
        field.send_keys(value)

    def set_checkbox(self, checked: bool = True) -> None:
        checkbox = self.wait_for_clickable(self.icecream_checkbox)
        if checkbox.is_selected() != checked:
            checkbox.click()

    def select_gender(self, gender_text: str) -> None:
        Select(self.wait_for_visible(self.gender_dropdown)).select_by_visible_text(gender_text)

    def submit(self) -> None:
        self.wait_for_clickable(self.submit_button).click()

    def get_success_message(self) -> str:
        return self.wait_for_visible(self.success_info).text

    def get_gender_options(self) -> list[str]:
        options = Select(self.wait_for_visible(self.gender_dropdown)).options
        return [opt.text.strip() for opt in options]

    @property
    def getName(self):  # noqa: N802
        return self.wait_for_visible(self.name_input)

    @property
    def getEmail(self):  # noqa: N802
        return self.wait_for_visible(self.email_input)

    @property
    def getCheckbox(self):  # noqa: N802
        return self.wait_for_clickable(self.icecream_checkbox)

    @property
    def getGender(self):  # noqa: N802
        return self.wait_for_visible(self.gender_dropdown)

    @property
    def submitForm(self):  # noqa: N802
        return self.wait_for_clickable(self.submit_button)

    @property
    def getSuccessMessage(self):  # noqa: N802
        return self.wait_for_visible(self.success_info)
