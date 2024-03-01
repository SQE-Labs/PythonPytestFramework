
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.BasePage import BasePage
from Config.config import TestData


class LoginPage(BasePage):
    NextButton = (By.ID,"idp-discovery-submit")
    OKTAUsernameField = (By.ID,"idp-discovery-username")
    OKTAPasswordField = (By.ID,"okta-signin-password")
    OKTASubmitButton = (By.ID,"okta-signin-submit")
    plusIconToCECRM = (By.XPATH,"//*[@class='app-header__new']")
    
    
    def __init__(self,driver, *args, **kwargs):
        super().__init__(driver, *args, **kwargs)
        self.driver.get(TestData.BASE_URL) 
        
    
    def login_Agency(self,username,passowrd):
        self.do_waitForElement_PresenceLocated(self.OKTAUsernameField)
        self.do_sendKeys(self.OKTAUsernameField,text=username)
        self.do_click(self.NextButton) 
        self.do_sendKeys(self.OKTAPasswordField,text=passowrd)
        self.do_click(self.OKTASubmitButton)  
        checkele = len(self.driver.find_elements(By.XPATH,"//h1[contains(text(),'Wait while we redirect you to your agency')]"))
        if(checkele > 0):
            WebDriverWait(self.driver,20).until(EC.invisibility_of_element(By.XPATH,"//h1[contains(text(),'Wait while we redirect you to your agency')]"))    
        
        self.do_waitForCursorInvisiblity(2)
        self.do_waitForElement_PresenceLocated(self.plusIconToCECRM)
        flag = self.is_elementVisible(self.plusIconToCECRM)
        assert flag
              
        
	
 
 
 
 
 
 
 
 
 
    
    