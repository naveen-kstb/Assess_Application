from selenium.webdriver.common.by import By


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    GlobalID =(By.CSS_SELECTOR, "input[placeholder='Global ID']")
    Password =(By.CSS_SELECTOR, "input[placeholder='Password']")
    SignIn =(By.CSS_SELECTOR, ".signin__btn")


    def getglobalid(self):
        return self.driver.find_element(*LoginPage.GlobalID)

    def getpassword(self):
        return self.driver.find_element(*LoginPage.Password)

    def getsignin(self):
        return self.driver.find_element(*LoginPage.SignIn)