import pytest
from selenium import webdriver
#import time


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


# Fixtures
@pytest.fixture(scope="class")
def setup(request):
  
    # Passing browser name in command Line
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(
            executable_path=".\\ChromeDriver\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="D:\\geckodriver.exe")
    elif browser_name == "IE":
        print("IE driver")
    driver.get("https://trello.com/")
    driver.maximize_window()

    request.cls.driver = driver
    # yield
    # driver.close()
