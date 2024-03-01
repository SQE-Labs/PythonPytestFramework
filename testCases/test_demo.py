import pytest
import unittest
from selenium import webdriver

class Tests_Demo(unittest.TestCase):
    def test_first(self):
        self.assertEqual(1,2)
    
    def test_second(self):
        self.assertEqual(1,1) 
        
    def test_third(self):
        self.assertEqual(True,True) 
        
    def test_fourth(self):
        self.assertEqual(True,False) 
    
    @pytest.mark.login    
    def test_fifth(self):
        self.assertEqual("Yes","yes") 
    
    @pytest.mark.login        
    def test_sixth(self):
        self.assertEqual(4>0,True)                    
        
        
if __name__ == '__main__':
    unittest.main()