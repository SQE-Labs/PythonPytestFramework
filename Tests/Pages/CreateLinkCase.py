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


class CreateCaseLink(BasePage):
    descriptionTextCSDP = (By.XPATH,"//div[@class='description tile'])/div[2]/div")
    attachmentsHeaderCSDP = (By.XPATH,"//div[@id='cs-attachments']//h2/span")
    addedCustomerCSDP = (By.XPATH,"//label[text()='Customer Name']/following::a[1]")
    submissionNumber = (By.XPATH,"//h2[@class='customer-submission-details__number']")
    moreButtonCSDP = (By.XPATH,"//button[text()='More...']")
    createAndLinkCaseOption = (By.XPATH,"//li[text()='Create & Link Case']")
    createACasePage = (By.XPATH,"//h1[text()='Create A Case']")
    issueDescriptionCCP = (By.XPATH,"//textarea[@name='issueDescription']")
    addedContactCCP = (By.XPATH,"//div[@class='contact__name-role']//b")
    attachmentHeaderCCP = (By.XPATH,"//div[@class='attachment-tile tile']//h2/span")
    locationSearchField = (By.XPATH,"//div[@class='location-tile__inputs-container']//input")
    locationSearchResults = (By.XPATH,"//div[@class='react-autosuggest__suggestion-element']")
    createCaseButton = (By.XPATH,"button.square-btn.space-left.btn.btn-primary")
    createCasePopup = (By.XPATH,"//div[text()='Create Case']")
    createScheduleInspectionButton = (By.XPATH,"//button[text()='Create & Schedule Inspection']")
    associatedSubmissionLink = (By.XPATH,"//label[text()='Associated Submission']/following::a[1]")
    linkedCaseNumber = (By.XPATH,"//h2[@class='case-details__case-number']")
    associatedCaseLink = (By.XPATH,"//label[text()='Associated Case']/following::a[1]")
    removeLink = (By.XPATH,"//a[text()='Remove Link']")
    
    
    def __init__(self,driver,*args,**kwargs):
        super().__init__(driver, *args, **kwargs)
        self.driver.get(TestData.BASE_URL)
       
        
    
    def test_CreateAndLinkCase_PreRequisite(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login_Agency(TestData.USERNAME,TestData.PASSWORD)
        self.createSubmission("No", "Yes", "Yes", "No", "Yes", "Location Not Required")
                