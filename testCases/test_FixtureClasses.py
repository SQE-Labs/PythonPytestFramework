
import pytest
from selenium import webdriver
import unittest

@pytest.fixture(scope='class')
def init_driver(request):
    ch_driver = webdriver.Chrome()
    request.cls.driver = ch_driver
    
    
@pytest.mark.usefixtures("init_driver")  
class Base_chrome_Test():
    pass    

class Test_ChromTestCases(Base_chrome_Test):
    
    def test_gooleTitle(self):
        self.driver.get("https://www.google.com/")
        self.driver.implicitly_wait(10)
        assert self.driver.title == "Google"