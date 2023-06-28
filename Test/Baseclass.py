import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class Baseclass:
    pass

    def WaitForGID(self):
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "input[placeholder='Global ID']")))

    def WaitForPassword(self):
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Password']")))

    def WaitForWelcomePage(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn")))

    def DragTheVideo(self):
        WebDriverWait.ActionChains(driver).click_and_hold(By.XPATH, "//ngx-slider[@aria-label='ngx-slider']").move_by_offset(100,0).perform()
