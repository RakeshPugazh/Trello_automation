from selenium.webdriver.common.by import By

from PageObjects.LoginPage import LoginPage
from Utilities.Utils import BaseClass


class LandingPage(BaseClass):

    def __init__(self, driver):  
        self.driver = driver

    #Locator
    LogInLinkLocator = (By.XPATH, "//a[@href='/login']")

    def ClickLogIn(self):   #Clicks on Login link from the Trello's Landing Page

        self.clickElement(LandingPage.LogInLinkLocator)
        loginPage = LoginPage(self.driver)
        return loginPage
