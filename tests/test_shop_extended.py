import pytest

from TestData.form_data import SHOP_PRODUCTS
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestShopExtended(BaseClass):
    @pytest.fixture
    def checkout_page(self):
        home = HomePage(self.driver)
        return home.open_shop()

    @pytest.mark.parametrize("product", SHOP_PRODUCTS)
    def test_product_present_in_catalog(self, checkout_page, product):
        titles = checkout_page.get_product_titles()
        assert product in titles

    @pytest.mark.parametrize("product", SHOP_PRODUCTS)
    def test_add_each_product_increments_cart_counter(self, checkout_page, product):
        initial = checkout_page.get_cart_count()
        checkout_page.add_product_to_cart(product)
        assert checkout_page.get_cart_count() == initial + 1

    def test_checkout_button_navigates_to_country_step(self, checkout_page):
        checkout_page.add_product_to_cart("Blackberry")
        checkout_page.open_cart()
        confirm = checkout_page.proceed_to_checkout()
        confirm.search_country("pol")
        confirm.select_country("Poland")
        confirm.complete_purchase()

        assert "Success! Thank you!" in confirm.get_alert_text()
