import time
from selenium import webdriver
import pytest


from selenium.webdriver.common.by import By

from PageObjects.LandingPage import LandingPage
from PageObjects.LoginPage import LoginPage
from PageObjects.BoardsPage import Boards
from TestData.Data import Data
from Utilities.Utils import BaseClass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestTrello(BaseClass):

    # Tests

    def test_LoginTrello(self, getUserData):

        landingPage = LandingPage(self.driver)
        loginPage = landingPage.ClickLogIn()
        loginPage.LogIn(getUserData["email"], getUserData["password"])

    @pytest.mark.group
    def test_CreateBoard(self):
        boards = Boards(self.driver)
        boards.CreateBoard("Trello_Board")

    @pytest.mark.group
    def test_CreateList(self, getListData):
        lists = Boards(self.driver)
        lists.CreateList(getListData)

    @pytest.mark.group
    def test_CreateCard(self, getCardData):
        cards = Boards(self.driver)
        cards.CreateCards("Not Started", getCardData)

    @pytest.mark.group
    def test_MoveCards(self):
        move = Boards(self.driver)
        move.MoveCards("Card 2", "In Progress")
        move.MoveCards("Card 3", "QA")
        move.MoveCards("Card 2", "QA")

    @pytest.mark.group
    def test_AssignUser(self):
        assign = Boards(self.driver)
        assign.AssignUser("Card 1", "I am done")


# Fixtures

    @pytest.fixture(params=[("Not Started", "In Progress", "QA", "Done")])
    def getListData(self, request):
        return request.param

    @pytest.fixture(params=[("Card 1", "Card 2", "Card 3", "Card 4")])
    def getCardData(self, request):
        return request.param

    @pytest.fixture(params=Data.test_data)
    def getUserData(self, request):
        return request.param
