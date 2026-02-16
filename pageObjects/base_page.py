from __future__ import annotations

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout

    def wait_for_visible(self, locator: tuple[str, str]) -> WebElement:
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator: tuple[str, str]) -> WebElement:
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_present(self, locator: tuple[str, str]) -> WebElement:
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_all_visible(self, locator: tuple[str, str]) -> list[WebElement]:
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )
