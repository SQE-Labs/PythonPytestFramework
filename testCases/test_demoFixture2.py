import pytest
from selenium import webdriver
import unittest


driver = None
def setup_module():
    global driver
    driver = webdriver.Chrome()
    driver.delete_all_cookies()
    driver.get("https://www.google.com/")
    driver.implicitly_wait(10)

def teardown_module():
    driver.quit()
    

def test_gooleTitle():
    assert driver.title == "Google"
                
    
def test_currentUrl():
    print(driver.current_url)
    assert driver.current_url == "https://www.google.com/"
            