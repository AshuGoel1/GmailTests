from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from GmailHelper import GmailHelper
import unittest

class GmailDeleteEmail(unittest.TestCase):
# Class to test deletion of a specific email in Gmail
    def setUp(self):
        self.driver = webdriver.Chrome()
        gmailHelper = GmailHelper(self.driver)
        gmailHelper.login()
        assert "Inbox" in self.driver.page_source
        self.driver.implicitly_wait(30)

    def testDeleteEmail(self):
        driver = self.driver
        emailSubject=driver.find_element_by_xpath("//span[text()='Test Email 2017-04-03 17:39:15.102827']")
        emailSubject.click()
        driver.implicitly_wait(30)
        assert "Test Email " in driver.page_source
        deleteEmail=driver.find_element_by_xpath("//*[@id=':5']/div[2]/div[1]/div/div[2]/div[3]")
        deleteEmail.click()
        driver.implicitly_wait(30)
        assert "The conversation has been moved to the Trash" in driver.page_source
        emailDeleteUndo = driver.find_element_by_xpath("//*[@id='link_undo']")
        emailDeleteUndo.click()
        driver.implicitly_wait(40)
        assert "Your action has been undone" in driver.page_source

    def tearDown(self):
        self.driver.close()

    if __name__ == "__main__":
        unittest.main()



