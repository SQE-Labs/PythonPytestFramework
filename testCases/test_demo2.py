import pytest
from selenium import webdriver
import unittest

class Tests_selnium(unittest.TestCase):
    def test_google(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/")
        driver.implicitly_wait(2)
        self.assertEqual(driver.title ,"Google")
        
    
    def test_selenium(self):
        driver = webdriver.Chrome()
        driver.get("https://www.selenium.dev/")
        driver.implicitly_wait(2)
        self.assertEqual(driver.title ,"Selenium")    
    
    def test_python(self):
        driver = webdriver.Chrome()
        driver.get("https://www.python.org/")
        driver.implicitly_wait(2)
        self.assertEqual(driver.title ,"Welcome to Python.org") 
        