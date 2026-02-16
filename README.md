# Python Selenium Framework (Modernized)

A Page Object Model (POM) UI test framework using **Python + Selenium 4 + Pytest**.

## What's inside

- POM-based page classes under `pageObjects/`
- Pytest fixtures and CLI options in `tests/conftest.py`
- Explicit waits (no brittle sleep-based synchronization)
- HTML report + screenshot-on-failure support
- Parametrized/data-driven tests
- Extended coverage for homepage + shop/checkout flows

## Prerequisites

- Python 3.10+
- Chrome or Firefox installed
- Internet access to `https://rahulshettyacademy.com/angularpractice/`

> Selenium Manager is used by default to provision drivers automatically.

## Installation

```bash
git clone https://github.com/apadlo/PythonSeleniumFramework.git
cd PythonSeleniumFramework
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run tests

### Run full suite (headless)
```bash
pytest -v --headless --html=reports/report.html --self-contained-html
```

### Run on Chrome / Firefox
```bash
pytest -v --browser_name chrome --headless
pytest -v --browser_name firefox --headless
```

### Run specific files
```bash
pytest -v tests/test_HomePage.py
pytest -v tests/test_e2e.py
pytest -v tests/test_homepage_extended.py
pytest -v tests/test_shop_extended.py
```

## Useful CLI options

- `--browser_name` : `chrome` (default) or `firefox`
- `--base-url` : override target URL
- `--headless` : run browser without UI

## Jenkins-ready commands

### Freestyle / Pipeline shell step
```bash
python -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pytest -v --headless --browser_name chrome \
  --junitxml=reports/junit.xml \
  --html=reports/report.html --self-contained-html
```

### Optional parallel run (if desired)
```bash
pytest -n auto -v --headless --browser_name chrome --junitxml=reports/junit.xml
```

## Project layout

- `pageObjects/` - POM classes
- `tests/` - pytest tests and fixture hooks
- `TestData/` - static and externalized test data
- `utilities/` - shared test utilities/base class
- `reports/` - generated reports and logs

## Notes

- Existing core tests are preserved and compatible.
- New tests are added with parametrization to improve coverage while keeping maintainability high.
