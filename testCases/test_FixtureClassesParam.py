
import pytest
from selenium import webdriver
import unittest

@pytest.fixture(params=['chrome','firefox'],scope='class')
def init_driver(request):
    if(request.param == 'chrome'):
        
        ch_driver = webdriver.Chrome()
        request.cls.driver = ch_driver
    
    
    if(request.param == 'firefox'):
        
        ch_driver = webdriver.Firefox()
        request.cls.driver = ch_driver
    
    yield
    ch_driver.quit()    
    
    
@pytest.mark.usefixtures("init_driver")  
class Base_chrome_Test():
    pass    

class Test_ChromTestCases(Base_chrome_Test):
    
    def test_gooleTitle(self):
        self.driver.get("https://www.google.com/")
        self.driver.implicitly_wait(2)
        assert self.driver.title == "Google"
    
    def test_goole_Url(self):
        self.driver.get("https://www.google.com/")
        self.driver.implicitly_wait(2)
        assert self.driver.current_url == "https://www.google.com/"
        