# Test Class for Feature Test
from TestClasses.test_Base import BaseTest
from Pages.LoginPage import LoginPage
from Config.config import TestData
import pytest
import allure


class Test_LoginPage(BaseTest):
    def test_Login_Agency(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login_Agency(TestData.USERNAME, TestData.PASSWORD)
        