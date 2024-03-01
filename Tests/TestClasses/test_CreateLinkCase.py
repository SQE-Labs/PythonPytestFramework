# Test Class for Feature Test
from TestClasses.test_Base import BaseTest
from Config.config import TestData
from Pages.CreateLinkCase import CreateCaseLink
import pytest
import allure



class Test_CreateLinkCase(BaseTest):
    
    def test_CreateAndLinkCase_PreRequisite(self):
        self.Create_LinkCase = CreateCaseLink(self.driver)
        self.Create_LinkCase.test_CreateAndLinkCase_PreRequisite()
    
    def test_CreateAndLinkCase_PreRequisite_second(self):
        self.Create_LinkCase = CreateCaseLink(self.driver)
        self.Create_LinkCase.test_CreateAndLinkCase_PreRequisite()    