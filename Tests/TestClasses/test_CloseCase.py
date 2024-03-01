# Test Class for Feature Test
from TestClasses.test_Base import BaseTest
from Config.config import TestData
from Pages.CloseCasePage import CloseCasePage
import pytest
import allure



class Test_CloseCase(BaseTest):
    
    def test_CloseCaseOpenCloseCasePopup(self):
        self.closeCase_Page = CloseCasePage(self.driver)
        self.closeCase_Page.test_CloseCaseOpenCloseCasePopup()
    
    
    def test_VerifyVoluntaryToggleBtnState(self):
        self.closeCase_Page = CloseCasePage(self.driver)
        self.closeCase_Page.test_VerifyVoluntaryToggleBtnState()
        
            