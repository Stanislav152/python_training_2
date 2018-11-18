# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group

class Test1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_1(self, group):
        driver = self.driver
        self.open_home_page(driver)
        self.manual_login(driver, username="admin", password="secret")
        self.open_group_page(driver)
        self.init_group_creation(driver)
        self.fill_group_form(driver, group(name="ppp"))
        self.submit_group_creation(driver)
        #open groups page
        #driver.find_element_by_link_text("groups").click()
        self.open_group_page(driver)
        self.logout(driver)

    """def test_1_empty(self):
        driver = self.driver
        self.open_home_page(driver)
        self.manual_login(driver, username="admin", password="secret")
        self.open_group_page(driver)
        self.init_group_creation(driver)
        self.fill_group_form(driver, Group(name=""))
        self.submit_group_creation(driver)
        #open groups page
        #driver.find_element_by_link_text("groups").click()
        self.open_group_page(driver)
        self.logout(driver)"""



    def logout(self, driver):
        # make logout
        driver.find_element_by_link_text("Logout").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")

    def submit_group_creation(self, driver):
        # submit group creation
        driver.find_element_by_name("submit").click()

    def fill_group_form(self, driver, Group):
        # fill group form
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(Group.name)

    def init_group_creation(self, driver):
        # init group creation
        driver.find_element_by_name("new").click()

    def open_group_page(self, driver):
        # open groups page
        driver.find_element_by_link_text("groups").click()

    def manual_login(self, driver, username, password):
        # waiting for manual login
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        #driver.find_element_by_xpath(
         #   "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()

    def open_home_page(self, driver):
        # open home page
        driver.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
