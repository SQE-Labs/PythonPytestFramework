
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config.config import TestData
import time

class BasePage:
    
    def __init__(self,driver,*args, **kwargs):
        self.driver = driver
    
    
    def do_waitForElement_PresenceLocated(self,by_locator):
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(by_locator))
    
    
    def do_waitForElement_Visiblity(self,by_locator):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
    
    def do_waitForElement_ElementClickable(self,by_locator):
        WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(by_locator))
    
    
    def do_clickByJSExecutor(self,by_locator):
        ele = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].click();", ele)
    
	   
    
    def do_click(self,by_locator):
        element= WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
        element.click()
    
    def do_sendKeys(self, by_locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element.send_keys(text) 
    
    def do_getText(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text   
    
    def is_elementVisible(self,by_locator):
            element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
            return element.is_displayed()
       
       
    def do_waitForCursorInvisiblity(self,tries,*args, **kwargs):
        for i in range(tries):
            
            try:   
                WebDriverWait(self.driver,60).until(EC.invisibility_of_element((By.XPATH,"//img[@src='/assets/loading.gif']")))
                break          
            except Exception as e:
                print(e)
                
    
    def scrollInto_view(self,by_locator):
        element = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(by_locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    
     
    def createSubmission(self,Anonymous,Customer,Tags,Location, Attachment,CategoryName,*args,**kwargs):  
        self.driver.get(TestData.CREAT_SUBMISSION_URL)
    
    def navigateToCCP(self):
        self.do_waitForElement_Visiblity((By.CSS_SELECTOR,"#header div.app-header__new"))
        self.do_waitForElement_PresenceLocated((By.CSS_SELECTOR,"#header div.app-header__new"))
        self.scrollInto_view((By.CSS_SELECTOR,"#header div.app-header__new"))
        self.do_waitForElement_ElementClickable((By.CSS_SELECTOR,"#header div.app-header__new"))
        self.do_waitForElement_ElementClickable((By.CSS_SELECTOR,"#header div.app-header__new"))
        self.do_clickByJSExecutor((By.CSS_SELECTOR,"#header div.app-header__new"))
        self.do_waitForElement_Visiblity((By.XPATH,"//label[text()='Code Enforcement Case']"))
        self.do_waitForElement_ElementClickable((By.XPATH,"//label[text()='Code Enforcement Case']"))
        self.do_clickByJSExecutor((By.XPATH,"//label[text()='Code Enforcement Case']"))
        self.do_waitForCursorInvisiblity(10)
        self.do_waitForElement_Visiblity((By.XPATH,"//h1[text()='Create A Case']"))
        self.do_waitForElement_PresenceLocated((By.XPATH,"//h1[text()='Create A Case']"))
        self.do_waitForElement_ElementClickable((By.XPATH,"//div/button[text()='Create Case']"))
    
    
    
    def serachLocationCCP(self,Address,*args,**kwargs):
        self.do_waitForElement_Visiblity((By.XPATH,"//div[@class='location-tile__inputs-container']//input"))
        self.do_waitForElement_ElementClickable((By.XPATH,"//div[@class='location-tile__inputs-container']//input"))
        self.do_sendKeys((By.XPATH,"//div[@class='location-tile__inputs-container']//input"), Address)
        self.do_waitForElement_Visiblity((By.XPATH,"//li[@id='react-autowhatever-1-section-0-item-0']"))
        self.do_waitForElement_Visiblity((By.XPATH,"//li[@id='react-autowhatever-1-section-0-item-0']"))
        self.do_waitForElement_ElementClickable((By.XPATH,"//li[@id='react-autowhatever-1-section-0-item-0']"))
        self.do_click((By.XPATH,"//li[@id='react-autowhatever-1-section-0-item-0']"))
        self.do_waitForCursorInvisiblity(10)

	
 
    def addViolationParam(self,vName,*args,**kwargs):
        time.sleep(3)
        self.do_waitForElement_Visiblity((By.XPATH,"//div/input[@placeholder=\"Start typing name of violation, article number or issue description\"]"))
        self.do_waitForElement_ElementClickable((By.XPATH,"//div/input[@placeholder=\"Start typing name of violation, article number or issue description\"]"))
        self.do_click((By.XPATH,"//div/input[@placeholder=\"Start typing name of violation, article number or issue description\"]"))
        time.sleep(5)
        self.do_waitForElement_Visiblity((By.XPATH,"//div/input[@placeholder=\"Start typing name of violation, article number or issue description\"]"))
        self.do_waitForElement_ElementClickable((By.XPATH,"//div/input[@placeholder=\"Start typing name of violation, article number or issue description\"]"))
        self.do_sendKeys((By.XPATH,"//div/input[@placeholder=\"Start typing name of violation, article number or issue description\"]"), vName)
        self.do_waitForElement_Visiblity((By.XPATH,"//div[@class='react-autosuggest__suggestion-element']/div"))
        self.do_waitForElement_ElementClickable((By.XPATH,"//div[@class='react-autosuggest__suggestion-element']/div"))
        self.do_click((By.XPATH,"//div[@class='react-autosuggest__suggestion-element']/div"))
    
    def addLocationCCP(self):
        self.serachLocationCCP(TestData.SEARCH_LOCATION)
    
    
    
    def addContact(self):
        pass
    
    
    
    
    def createCase(self):
        self.navigateToCCP()
        self.addLocationCCP()
        self.addViolationParam("Wa")
        time.sleep(5)
        self.addContact()
        self.do_waitForElement_ElementClickable((By.XPATH,"//div/button[text()='Create Case']"))
        self.do_click((By.XPATH,"//div/button[text()='Create Case']"))
        time.sleep(5)

        if len(self.driver.find_elements(By.XPATH, "//button[text()='Close']")) >= 1:
            self.do_click((By.XPATH, "//button[text()='Close']"))

            keep_contacts = self.driver.find_elements(By.XPATH, "//button[text()='Keep contact']")
            size = len(keep_contacts)

            if size >= 1:
                for element in keep_contacts:
                    self.scroll_into_view(element)
                    element.click()
            
            self.do_waitForElement_ElementClickable((By.XPATH,"//div/button[text()='Create Case']"))
            self.do_click((By.XPATH,"//div/button[text()='Create Case']"))
				

			

       
        self.do_waitForCursorInvisiblity(5)
        self.do_waitForElement_Visiblity((By.XPATH, "//h5[text()='Assign Case To']//parent::div//button[@class='square-btn btn btn-primary']"))
        self.do_waitForElement_PresenceLocated((By.XPATH, "//h5[text()='Assign Case To']//parent::div//button[@class='square-btn btn btn-primary']"))
        self.do_waitForElement_Visiblity((By.XPATH,"//h5[text()='Assign Case To']//parent::div//button"))
        self.do_waitForElement_ElementClickable((By.XPATH,"//h5[text()='Assign Case To']//parent::div//button"))
        self.do_click((By.XPATH,"//h5[text()='Assign Case To']//parent::div//button"))
        self.do_waitForElement_ElementClickable((By.XPATH,"//h5[text()='Assign Case To']//parent::div//button"))
        self.do_click((By.XPATH,"//h5[text()='Assign Case To']//parent::div//button"))
        self.do_waitForElement_ElementClickable((By.XPATH,"//div[@class='modal-footer']//button[2]"))
        self.do_click((By.XPATH,"//div[@class='modal-footer']//button[2]"))
        self.do_waitForCursorInvisiblity(10)   
                
         