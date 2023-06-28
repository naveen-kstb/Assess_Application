from selenium.webdriver.common.by import By


class WelcomePage():

    def __init__(self, driver):
        self.driver = driver

    Button =(By.CSS_SELECTOR, ".btn")
    Watch =(By.CSS_SELECTOR, "div[class='watch-btn'] button span")
    Play =(By.CSS_SELECTOR, ".icon-play-circle")
    Drag =(By.XPATH, "//ngx-slider[@aria-label='ngx-slider']")

    def getWelcomePage(self):
        return self.driver.find_element(*WelcomePage.Button)

    def getWatch(self):
        return self.driver.find_element(*WelcomePage.Watch)

    def getPlay(self):
        return self.driver.find_element(*WelcomePage.Drag)

    def getDrag(self):
        return self.driver.find_element(*WelcomePage.Play)