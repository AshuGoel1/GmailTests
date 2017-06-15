from selenium import webdriver
from GmailHelper import GmailHelper
import unittest

class GmailAdvancedSearch(unittest.TestCase):
    """To test 'Advanced Search' in Gmail """

    def setUp(self):
        self.driver = webdriver.Chrome()
        gmailHelper = GmailHelper(self.driver)
        gmailHelper.login()
        assert "Inbox" in self.driver.page_source
        self.driver.implicitly_wait(30)

    def testAdvancedSearch(self):
        driver = self.driver
        searchBoxXpath = driver.find_element_by_xpath("//input[@aria-label='Search']")
        searchBoxXpath.click()
        searchBoxXpath.send_keys("subject:(Test Email)")
        searchBoxBlueButtonXpath = driver.find_element_by_xpath("//div/button[@aria-label='Search Gmail']")
        searchBoxBlueButtonXpath.click()
        driver.implicitly_wait(30)
        assert "No messages matched your search" not in driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()