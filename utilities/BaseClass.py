from __future__ import annotations

import inspect
import logging
from pathlib import Path

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def wait_for_presence(self, locator: tuple[str, str], timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_for_visible(self, locator: tuple[str, str], timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator: tuple[str, str], timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def verifyLinkPresence(self, locator, text):  # noqa: N802
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator, text)))

    @staticmethod
    def selectOptionByText(locator, text):  # noqa: N802
        Select(locator).select_by_visible_text(text)

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        logs_dir = Path("reports") / "logs"
        logs_dir.mkdir(parents=True, exist_ok=True)
        handler = logging.FileHandler(logs_dir / "test.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        handler.setFormatter(formatter)

        logger.handlers.clear()
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        return logger
