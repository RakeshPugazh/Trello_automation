import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Utilities.Utils import BaseClass
#


class LoginPage(BaseClass):

    Base = BaseClass()
    log = Base.getLogger()

    def __init__(self, driver):  
        self.driver = driver

    #Locators
    InputEmailLocator = (By.XPATH, "//input[@id='user']")
    LogInWithAtlassianLocator = (By.ID, "login")
    InputPasswordLocator = (By.ID, "password")
    LoginButton = (By.ID, "login-submit")

    def LogIn(self, email, password):  #Accepts & Enters email and password.And LogIn to Trello

        self.sendText(LoginPage.InputEmailLocator, email)   #Pass Email
        time.sleep(5)
        self.clickElement(LoginPage.LogInWithAtlassianLocator)
        self.sendText(LoginPage.InputPasswordLocator, password)  #Pass Password
        self.clickElement(LoginPage.LoginButton)
        self.log.info("Logged In Successfully ")
