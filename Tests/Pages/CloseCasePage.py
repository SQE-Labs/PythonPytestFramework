import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage
from Config.config import TestData
from Pages.LoginPage import LoginPage
import allure
from allure_commons.types import AttachmentType
import time
from datetime import datetime


class CloseCasePage(BasePage):
    closeCaseBtn = (By.CSS_SELECTOR,"ul.dropdown-button__dropdown-wrap>li:first-child")
    closeCasePopup = (By.XPATH,"//div[@class='modal-header' and text()='Close Case']")
    cancelBtnCCPopup = (By.XPATH,"//button[text()='Cancel']")
    voluntaryBtn =(By.XPATH, "//button[text()='Voluntary']")
    closeCaseBtnCCPopup = (By.XPATH,"//button[text()='Close Case']")
    yesBtnConfirmationPopup =(By.XPATH, "//div[@class='flex-row--center']/button[text()='Yes']")
    closedStatus =(By.XPATH, "//h2[text()='Closed']")
    closeCDPIcon = (By.XPATH,"//div[@class='case-details__close-icon']")
    performInsBtn = (By.XPATH,"//button[text()='Perform Inspection']")
    invalidBtnlist = (By.XPATH,"//div[@class='multi-choice-buttons']/button[text()='Invalid']")
    yesConfirmation = (By.XPATH,"//div[@class='flex-row--center']/button[text()='Yes']")
    moreBtn = (By.XPATH,"//button[contains(text(),'More...')]")
    reopenCaseOpt = (By.XPATH,"//li[text()='Reopen Case']")
    reopenCaseButton = (By.XPATH,"//button[text()='Reopen Case']")
    nonCompliantButton = (By.XPATH,"//button[text()='Non-Compliant']")
    voluntaryBtn = (By.XPATH,"//button[text()='Voluntary']")
    forcedToggle=(By.XPATH,"//div[@class='multi-choice-buttons']/button[text()='Forced']")
    forced_Toggle="//div[@class='multi-choice-buttons']/button[text()='Forced']"
    voluntary_Btn = "//button[text()='Voluntary']"
    
    
     
    def __init__(self,driver,*args, **kwargs):
        super().__init__(driver, *args, **kwargs)
        #self.driver.get(TestData.BASE_URL)
    
    def test_CloseCaseOpenCloseCasePopup(self):
        self.driver.get(TestData.BASE_URL)
        self.login_page = LoginPage(self.driver)
        self.login_page.login_Agency(TestData.USERNAME,TestData.PASSWORD)
        self.createCase()
        self.do_waitForElement_ElementClickable(self.performInsBtn)
        self.do_click(self.performInsBtn)
        self.do_waitForElement_ElementClickable(self.invalidBtnlist)
        self.do_click(self.invalidBtnlist)
        self.do_waitForElement_ElementClickable((By.XPATH,"//button[text()='Complete Inspection & Close Case']"))
        self.do_click((By.XPATH,"//button[text()='Complete Inspection & Close Case']"))
        self.do_waitForElement_ElementClickable(self.yesConfirmation)
        self.do_click(self.yesConfirmation)
        self.do_waitForCursorInvisiblity(5)
        self.do_waitForElement_Visiblity(self.moreBtn)
        self.do_waitForElement_ElementClickable(self.moreBtn)
        self.do_click(self.moreBtn)
        self.do_waitForElement_ElementClickable(self.reopenCaseOpt)
        self.do_click(self.reopenCaseOpt)
        self.do_waitForElement_ElementClickable(self.nonCompliantButton)
        self.do_click(self.nonCompliantButton)
        self.do_waitForElement_ElementClickable(self.reopenCaseButton)
        self.do_click(self.reopenCaseButton)
        self.do_waitForCursorInvisiblity(5)
        self.do_waitForElement_Visiblity(self.moreBtn)
        self.do_waitForElement_ElementClickable(self.moreBtn)
        self.do_click(self.moreBtn)
        self.do_waitForElement_Visiblity(self.closeCaseBtn)   
    
    
    
    def test_VerifyVoluntaryToggleBtnState(self):
        self.do_waitForElement_Visiblity(self.closeCaseBtn)
        self.do_waitForElement_ElementClickable(self.closeCaseBtn)
        self.do_click(self.closeCaseBtn)
        self.do_waitForElement_Visiblity((By.XPATH,"//div[@class='multi-choice-buttons']//button[@class='square-btn btn btn-primary']"))
        self.do_waitForElement_PresenceLocated((By.XPATH,"//div[@class='multi-choice-buttons']//button[@class='square-btn btn btn-primary']"))
        VoluntaryBtnState = self.driver.find_element(By.XPATH,self.voluntary_Btn)
        self.do_waitForElement_PresenceLocated(self.forcedToggle)
        ForcedBtnState = self.driver.find_element(By.XPATH,self.forced_Toggle)
        assert ForcedBtnState.is_enabled()
        assert VoluntaryBtnState.is_enabled()
      

			 