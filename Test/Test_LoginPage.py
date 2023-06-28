import time

import pytest

from PageObjects.LoginPage import LoginPage
from PageObjects.WelcomePage import WelcomePage
from TestData.LoginPageData import HomePageData
from Test.Baseclass import Baseclass


class TestLoginPage(Baseclass):

    def test_loginpage(self, getData):
        loginpage = LoginPage(self.driver)
        self.WaitForGID()
        loginpage.getglobalid().send_keys(getData["GID"])
        self.WaitForPassword()
        loginpage.getpassword().send_keys(getData["Password"])
        loginpage.getsignin().click()

        welcomepage = WelcomePage(self.driver)
        self.WaitForWelcomePage()
        welcomepage.getWelcomePage().click()

        welcomepage.getWatch().click()

        welcomepage.getPlay().click()
        welcomepage.getDrag()
        self.DragTheVideo()

    # @pytest.fixture(params=[("Naveen", "hello@gmail.com", "Male"), ("Saisha", "hello@gmail.com", "Female")])
    @pytest.fixture(params=HomePageData.getTestData("Testcase 1"))
    def getData(self, request):
        return request.param
