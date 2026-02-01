# 🚀 Python Selenium Test Automation Framework

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green.svg)](https://www.selenium.dev/)
[![pytest](https://img.shields.io/badge/pytest-Framework-orange.svg)](https://pytest.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A comprehensive, production-ready test automation framework built with Python and Selenium WebDriver, implementing industry best practices including the Page Object Model (POM) design pattern, data-driven testing, and robust reporting capabilities.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Reports and Logging](#reports-and-logging)
- [Configuration](#configuration)
- [Best Practices Implemented](#best-practices-implemented)
- [Contributing](#contributing)

---

## 🎯 Overview

This framework demonstrates a scalable and maintainable approach to web application test automation. It showcases professional testing practices suitable for enterprise-level applications, featuring modular design, reusable components, and comprehensive test coverage.

**Learning Source:** Based on "Selenium WebDriver with Python" course by Rahul Shetty Academy

---

## ✨ Key Features

### Core Capabilities
- ✅ **Page Object Model (POM)**: Clean separation of test logic and page elements
- ✅ **Data-Driven Testing**: Parameterized tests with external data sources
- ✅ **Multi-Browser Support**: Chrome, Firefox, and Internet Explorer compatibility
- ✅ **Cross-Platform**: Works on Windows, macOS, and Linux
- ✅ **HTML Reports**: Beautiful, detailed test execution reports with screenshots
- ✅ **Logging Framework**: Comprehensive logging for debugging and analysis
- ✅ **Screenshot on Failure**: Automatic screenshot capture for failed tests
- ✅ **Explicit Waits**: Robust synchronization mechanisms
- ✅ **Modular Architecture**: Highly maintainable and extensible codebase

### Advanced Features
- 🔧 Pytest fixtures for setup and teardown
- 🔧 Custom utilities and helper methods
- 🔧 Command-line arguments for flexible test execution
- 🔧 Integration-ready for CI/CD pipelines (Jenkins, GitHub Actions, etc.)
- 🔧 Excel integration for test data management

---

## 🏗️ Architecture

The framework follows the **Page Object Model (POM)** design pattern, which provides:

```
┌─────────────────┐
│   Test Cases    │  ← High-level test scenarios
└────────┬────────┘
         │
    ┌────▼─────┐
    │   Base   │  ← Common utilities & fixtures
    │  Class   │
    └────┬─────┘
         │
┌────────▼─────────┐
│  Page Objects    │  ← Page-specific elements & methods
└──────────────────┘
         │
    ┌────▼─────┐
    │ WebDriver│  ← Browser automation
    └──────────┘
```

**Benefits:**
- Reduced code duplication
- Easy maintenance when UI changes
- Improved test readability
- Better separation of concerns
- Reusable components

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Programming Language** | Python 3.8+ |
| **Web Automation** | Selenium WebDriver 4.x |
| **Testing Framework** | Pytest |
| **Reporting** | pytest-html |
| **Data Management** | openpyxl (Excel integration) |
| **Logging** | Python logging module |
| **Browsers** | Chrome, Firefox, Internet Explorer |

---

## 📁 Project Structure

```
PythonSeleniumFramework/
│
├── pageObjects/              # Page Object Model classes
│   ├── HomePage.py          # Home page elements and methods
│   ├── CheckoutPage.py      # Checkout page elements and methods
│   └── ConfirmPage.py       # Confirmation page elements and methods
│
├── tests/                    # Test cases
│   ├── conftest.py          # Pytest configurations and fixtures
│   ├── test_HomePage.py     # Home page test scenarios
│   └── test_e2e.py          # End-to-end test scenarios
│
├── utilities/                # Helper utilities
│   └── BaseClass.py         # Base class with common methods
│
├── TestData/                 # Test data files
│   ├── HomePageData.py      # Home page test data
│   └── excelDemo.py         # Excel data integration examples
│
├── reports/                  # Generated test reports
│   └── assets/              # Report assets (CSS, JS)
│
└── README.md                # Project documentation
```

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Web browsers (Chrome/Firefox/IE)
- Corresponding WebDriver executables

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/apadlo/PythonSeleniumFramework.git
   cd PythonSeleniumFramework
   ```

2. **Install dependencies**
   ```bash
   pip install selenium pytest pytest-html openpyxl
   ```

3. **Download WebDrivers**
   - [ChromeDriver](https://chromedriver.chromium.org/)
   - [GeckoDriver (Firefox)](https://github.com/mozilla/geckodriver/releases)
   - [IEDriver](https://www.selenium.dev/downloads/)

4. **Add WebDrivers to PATH**
   - Place the driver executables in a directory included in your system PATH
   - Or specify the driver path in the code

---

## 🚀 Usage

### Basic Test Execution

Run all tests with default browser (Chrome):
```bash
pytest tests/
```

### Run Specific Test File
```bash
pytest tests/test_e2e.py
```

### Run with Specific Browser
```bash
pytest tests/ --browser_name firefox
pytest tests/ --browser_name chrome
pytest tests/ --browser_name ie
```

### Generate HTML Report
```bash
pytest tests/ --html=reports/report.html --self-contained-html
```

### Run with Verbose Output
```bash
pytest tests/ -v -s
```

### Run Specific Test Method
```bash
pytest tests/test_HomePage.py::TestHomePage::test_formSubmission -v
```

---

## 🧪 Running Tests

### End-to-End Test Example
The framework includes a complete e-commerce workflow test:
```python
# test_e2e.py demonstrates:
- Navigate to shop
- Add product to cart
- Proceed to checkout
- Enter shipping information
- Complete purchase
- Verify success message
```

### Data-Driven Test Example
Form submission test with multiple data sets:
```python
# test_HomePage.py demonstrates:
- Parameterized testing
- Multiple user scenarios
- Form validation
- Dynamic data handling
```

---

## 📊 Reports and Logging

### HTML Reports
- **Location**: `reports/report.html`
- **Features**:
  - Test execution summary
  - Pass/Fail status
  - Execution time
  - Screenshots for failed tests
  - Detailed error messages

### Logs
- **Location**: `tests/logfile.log`
- **Content**:
  - Timestamp
  - Log level (INFO, DEBUG, ERROR)
  - Test method name
  - Custom messages

### Screenshots
- Automatically captured on test failure
- Embedded in HTML reports
- Named with test method identifier

---

## ⚙️ Configuration

### Browser Configuration
Modify `conftest.py` to add or modify browser configurations:
```python
@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    # Add more browsers as needed
```

### Test Data Configuration
Update `TestData/HomePageData.py` to modify test data:
```python
test_HomePage_data = [
    {"firstname": "John", "email": "john@example.com", "gender": "Male"},
    {"firstname": "Jane", "email": "jane@example.com", "gender": "Female"}
]
```

---

## 🎓 Best Practices Implemented

### Design Patterns
- ✅ **Page Object Model**: Separation of test logic and UI
- ✅ **DRY Principle**: Reusable utilities in BaseClass
- ✅ **Single Responsibility**: Each page object manages only its page

### Test Design
- ✅ **Independent Tests**: No test dependencies
- ✅ **Descriptive Names**: Clear test method naming
- ✅ **Setup/Teardown**: Proper resource management
- ✅ **Explicit Waits**: Reliable element synchronization

### Code Quality
- ✅ **Modular Structure**: Easy to navigate and maintain
- ✅ **Centralized Configuration**: Single source for settings
- ✅ **Error Handling**: Robust exception management
- ✅ **Logging**: Comprehensive debugging information

### Reporting
- ✅ **Visual Reports**: HTML reports with screenshots
- ✅ **Detailed Logs**: Timestamped execution logs
- ✅ **Failure Tracking**: Automatic screenshot on failure

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve this framework:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 Topics Covered

This framework demonstrates practical implementation of:

- ✅ Python programming fundamentals
- ✅ Python data types and OOP concepts
- ✅ Selenium locator strategies (ID, Name, CSS, XPath, Link Text)
- ✅ Multi-browser test execution
- ✅ Selenium API methods and user interactions
- ✅ Advanced user interactions (dropdowns, checkboxes, forms)
- ✅ End-to-end test scenarios
- ✅ PyTest framework fundamentals
- ✅ Pytest fixtures and parameterization
- ✅ Pytest annotations and command-line arguments
- ✅ HTML report generation
- ✅ Logging implementation
- ✅ Page Object Model design pattern
- ✅ Framework design from scratch
- ✅ Data-driven testing with Excel
- ✅ openpyxl library integration
- ✅ CI/CD integration concepts (Jenkins, GitHub)
- ✅ Version control with Git/GitHub

---

## 📧 Contact

**Author**: [Your Name]

**Portfolio**: [Your Portfolio Link]

**LinkedIn**: [Your LinkedIn]

**Email**: [Your Email]

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🌟 Acknowledgments

- **Rahul Shetty Academy** for the comprehensive Selenium with Python course
- The **Selenium** and **Pytest** communities for excellent documentation
- All contributors and testers who help improve this framework

---

<div align="center">

**⭐ Star this repository if you find it helpful!**

Made with ❤️ and Python 🐍

</div>
