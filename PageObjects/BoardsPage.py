from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.LoginPage import LoginPage
from Utilities.Utils import BaseClass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class Boards(BaseClass):

    Base = BaseClass()
    log = Base.getLogger()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Create Board Locators
    CreateButtonLocator = (
        By.XPATH, "//button[@data-test-id='header-create-menu-button']")

    CreateBoardLocator = (
        By.XPATH, "//button[@data-test-id='header-create-board-button']")

    InputBoardTitleLocator = (
        By.XPATH, "//input[@data-test-id='create-board-title-input']")
    BoardCreateButtonLocator = (
        By.XPATH, "//button[@data-test-id='create-board-submit-button']")

    # Create List Locators
    AddListContainerLocator = (
        By.XPATH, "//div[@class ='js-add-list list-wrapper mod-add is-idle']")

    AddListWrapperLocator = (
        By.XPATH, "//div[@class='js-add-list list-wrapper mod-add']")

    InputListTitleLocator = (
        By.XPATH, "//input[@class='list-name-input']")
    AddListButtonLocator = (
        By.XPATH, "//div[@class='list-add-controls u-clearfix']/input")

    ListContainerLocator = (
        By.XPATH, "//div[@class='js-list list-wrapper']")

    TextAreaEXTLocator = (By.XPATH, "div/div/textarea")
    # Add Cards Locators
    AddCardContainerEXTLocator = (By.XPATH, "div/div[3]/a")

    CardTitleEXTLocator = (By.XPATH, "div/div[2]/div/div[1]/div/textarea")
    AddCardButtonEXTLocator = (
        By.XPATH, "div/div[2]/div/div[2]/div/input")

    CardContainerLocator = (
        By.XPATH, "//div[@class='list-card-details js-card-details']")

    CardNameExtLocator = (By.XPATH, "span")
    # Move Cards Locators
    MoveDropdownLocator = (By.XPATH, "//select[@class='js-select-list']")
    MoveOptionLocator = (
        By.XPATH, "//a[@class='quick-card-editor-buttons-item js-move-card']")
    MoveSubmitLocator = (
        By.XPATH, "//input[@class='nch-button nch-button--primary wide js-submit']")
    # Assign User and Comment Locators
    ProfileLocator = (
        By.XPATH, "//button[@data-test-id='header-member-menu-button']/div/span")
    ProfileNameLocator = (
        By.XPATH, "//div[@class='_2LKdO6O3n25FhC']")
    ProfileCloseButtonLocator = (
        By.XPATH, "//div[@class='_2LKdO6O3n25FhC']")
    MembersLocator = (
        By.XPATH, "//div[@class='window-module u-clearfix']/div/a[1]")
    BoardMembersLocator = (
        By.XPATH, "//ul[@class='pop-over-member-list checkable u-clearfix js-mem-list']/li")
    BoardMemberNameExtLocator = (By.XPATH, "a")
    MembersCloseLocator = (
        By.XPATH, "//div[@class='pop-over-header js-pop-over-header']/a")
    CommentBoxLocator = (By.XPATH, "//div[@class='comment-box']/textarea")
    CommentSaveLocator = (By.XPATH, "//div[@class='comment-box']/div[1]/input")

    def CreateBoard(self, BoardName):  # Creates new Board
        self.clickElement(Boards.CreateButtonLocator)
        self.checkVisibilityAndCLick(Boards.CreateBoardLocator)
        self.sendText(Boards.InputBoardTitleLocator, BoardName)
        self.clickElement(Boards.BoardCreateButtonLocator)
        self.log.info(BoardName + " has been created")

    def CreateList(self, getListData):  # Created List in boards
        listcount = len(getListData)
        for i in range(listcount):
            self.waitUntilPresence(Boards.AddListWrapperLocator)
            self.sendText(Boards.InputListTitleLocator, getListData[i])
            self.clickElement(Boards.AddListButtonLocator)
            self.log.info(getListData[i] + " List has been created")

    def CreateCards(self, ExpListName, getCardData):  # Creates 4 cards in List
        # time.sleep(2)
        self.waitUntilPresence(Boards.ListContainerLocator)
        Lists = self.driver.find_elements(*Boards.ListContainerLocator)
        for List in Lists:
            ListName = List.find_element(*Boards.TextAreaEXTLocator).text
            if ListName == ExpListName:
                List.find_element(*Boards.AddCardContainerEXTLocator).click()
                Cards = len(getCardData)
                for i in range(Cards):
                    print("Add CardName:", getCardData[i])
                    List.find_element(*Boards.CardTitleEXTLocator).send_keys(
                        getCardData[i])
                    List.find_element(*Boards.AddCardButtonEXTLocator).click()
                    time.sleep(3)
                    self.log.info(getCardData[i] + " has been created")

    def MoveCards(self, CardName, ListName):  # Move cards between lists
        Cards = self.driver.find_elements(*Boards.CardContainerLocator)
        action = ActionChains(self.driver)
        for Card in Cards:
            # time.sleep(3)
            ActualCardName = Card.find_element(*Boards.CardNameExtLocator).text
            if ActualCardName == CardName:
                action.context_click(Card).perform()
                self.clickElement(Boards.MoveOptionLocator)
                dropdownelement = self.driver.find_element(
                    *Boards.MoveDropdownLocator)
                self.selectOptionsByText(dropdownelement, ListName)
                self.clickElement(Boards.MoveSubmitLocator)
                self.log.info(CardName + " moved to " + ListName + " List")

    def AssignUser(self, CardName, Comment):
        self.clickElement(Boards.ProfileLocator)
        CurrentUser = self.driver.find_element(
            *Boards.ProfileNameLocator).get_attribute("title")
        self.clickElement(Boards.ProfileCloseButtonLocator)

        Cards = self.driver.find_elements(*Boards.CardContainerLocator)

        for Card in Cards:  # Loops through the cards, finds the required card & Adds member and posts comment

            ActualCardName = Card.find_element(*Boards.CardNameExtLocator).text
            print(ActualCardName, CardName)

            if ActualCardName == CardName:
                Card.click()
                self.clickElement(Boards.MembersLocator)
                BoardMembers = self.driver.find_elements(
                    *Boards.BoardMembersLocator)
                action = ActionChains(self.driver)
                for BoardMember in BoardMembers:
                    MemberName = BoardMember.find_element(
                        *Boards.BoardMemberNameExtLocator).get_attribute("title")
                    if CurrentUser == MemberName:
                        action.move_to_element(BoardMember).click().perform()
                        self.clickElement(Boards.MembersCloseLocator)
                self.log.info(CardName + " has been assigned to " + MemberName)
        # Comments
        self.sendText(Boards.CommentBoxLocator, Comment)
        self.clickElement(Boards.CommentSaveLocator)
        self.log.info("Commented - " + Comment)
