import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass():

    def clickElement(self, locator): #waits until the element is clickable and perform click operation
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((locator))).click()

    def sendText(self, locator, value): #Enter values in input fields
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((locator))).send_keys(value)

    def waitUntilPresence(self, locator): #waits until the presence of an element
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (locator)))

    def checkVisibilityAndCLick(self, locator):  #Checks for the visibility of an element and perform click  operation
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (locator))).click()

    def selectOptionsByText(self, locator, text): #Accepts locator and dropdown option to be selected.
        print(locator)
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)  

    def getLogger(self):   #Logger 
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler(
            '.\\Result\\Logs\\automationLogs.log')
        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  
        logger.setLevel(logging.DEBUG)
        return logger

    def wait(self):
        self.driver.implicitly_wait(10)
