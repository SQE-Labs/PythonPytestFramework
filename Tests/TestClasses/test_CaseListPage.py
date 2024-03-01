# Test Class for Feature Test
from TestClasses.test_Base import BaseTest
from Config.config import TestData
from Pages.CaseListPage import CaseListPage
import pytest
import allure



class Test_CaseListPage(BaseTest):
    
    def test_CaseListPage(self):
        self.caseList_page = CaseListPage(self.driver)
        self.caseList_page.test_NavigateToCaseListPage()
      
        
    
    # @pytest.mark.skip
    # def test_skipThisTest():
    #     print("in the skipped test")
    #     assert True    
            
    # @pytest.mark.xfail    
    # def test_ExpectedFailAndPass():
    #     print("ExpectedFaile Marker")
    #     assert False
    
    # @pytest.mark.parametrize("username,password",[("arun","123"),("arun","1234"),("arun","12345")])
    # def test_Parameterized(self,username,password): 
    #     print(username+" "+password)
            
    
    # @pytest.mark.Regression
    # def test_Sample1(self):
    #     print("test 1 Regression")  
    
    
    # @pytest.mark.Smoke
    # def test_Sample2(self):
    #     print("test 2 Smoke")  
        
    # @pytest.mark.Regression
    # def test_Sample3(self):
    #     print("test 3 Regression")
        
    # @pytest.mark.Smoke
    # def test_Sample4(self):
    #     print("test 4 Smoke")                      