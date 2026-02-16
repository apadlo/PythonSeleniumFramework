import pytest

from TestData.form_data import ALERT_KEYWORDS, FORM_DATA
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePageExtended(BaseClass):
    @pytest.mark.parametrize("data", FORM_DATA)
    def test_form_submission_with_multiple_datasets(self, data):
        home = HomePage(self.driver)
        home.fill_name(data["firstname"])
        home.fill_email(data["email"])
        home.set_checkbox(True)
        home.select_gender(data["gender"])
        home.submit()

        assert "Success! The Form has been submitted successfully" in home.get_success_message()
        self.driver.get(self.driver.current_url)

    def test_gender_dropdown_has_expected_values(self):
        home = HomePage(self.driver)
        options = home.get_gender_options()
        assert "Male" in options
        assert "Female" in options

    def test_checkbox_is_toggleable(self):
        home = HomePage(self.driver)
        home.set_checkbox(False)
        assert home.getCheckbox.is_selected() is False
        home.set_checkbox(True)
        assert home.getCheckbox.is_selected() is True

    def test_shop_navigation_works(self):
        home = HomePage(self.driver)
        home.open_shop()
        assert "shop" in self.driver.current_url

    @pytest.mark.parametrize("keyword", ALERT_KEYWORDS)
    def test_success_message_contains_expected_keywords(self, keyword):
        # Previous test may leave us on /shop; reset to form page first.
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        home = HomePage(self.driver)

        # Extra guard for CI flakiness: ensure form is visible before interacting.
        home.wait_for_visible(home.name_input, timeout=20)

        home.fill_name("KeywordUser")
        home.fill_email("keyword@example.com")
        home.set_checkbox(True)
        home.select_gender("Female")
        home.submit()

        assert keyword in home.get_success_message()
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
