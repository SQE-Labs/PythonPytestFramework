# For Fixture 

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import allure
from allure_commons.types import AttachmentType


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):    
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.yield_fixture
def log_on_failure(request):
    msgs = []
    yield msgs.append
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)        


@pytest.fixture(params=['chrome'],scope='class')
def init_driver(request):
    global driver
    if request.param == 'chrome':
        chrome_option = Options()
        chrome_option.add_experimental_option("detach",True)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_option)
        driver.maximize_window()
   
    
    request.cls.driver = driver
    yield
    #driver.quit()
    