from __future__ import annotations

from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="chrome|firefox")
    parser.addoption("--base-url", action="store", default="https://rahulshettyacademy.com/angularpractice/")
    parser.addoption("--headless", action="store_true", help="Run browsers in headless mode")


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser_name").lower()
    base_url = request.config.getoption("--base-url")
    headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        driver = webdriver.Firefox(options=options)
        driver.set_window_size(1920, 1080)
    else:
        raise ValueError(f"Unsupported browser_name: {browser_name}")

    driver.implicitly_wait(0)
    driver.get(base_url)

    request.cls.driver = driver
    yield
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when in {"setup", "call"} and report.failed and not hasattr(report, "wasxfail"):
        driver = getattr(item.instance, "driver", None)
        if driver is not None:
            screenshots_dir = Path("reports") / "screenshots"
            screenshots_dir.mkdir(parents=True, exist_ok=True)
            file_name = f"{report.nodeid.replace('::', '_').replace('/', '_')}.png"
            file_path = screenshots_dir / file_name
            driver.save_screenshot(str(file_path))
            if pytest_html:
                extras.append(pytest_html.extras.png(file_path.read_bytes(), mime_type="image/png"))

    report.extras = extras
