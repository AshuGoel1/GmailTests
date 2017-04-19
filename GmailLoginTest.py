from GmailHelper import GmailHelper
import unittest
from selenium import webdriver

class GmailLoginTest(unittest.TestCase):
    """To test postive and negative login credentials"""

    def setUp(self):
        self.driver = webdriver.Chrome()

    def testGmailValidPassword(self):
        gmailHelper = GmailHelper(self.driver)
        gmailHelper.login()
        assert "Inbox" in self.driver.page_source
        self.driver.implicitly_wait(30)
        signOutXpath=self.driver.find_element_by_xpath("//*[@id='gb']/div[1]/div[1]/div[2]/div[4]/div[1]/a/span")
        signOutXpath.click()
        signOut=self.driver.find_element_by_id("gb_71")
        signOut.click()
        assert "Sign in to continue to Gmail" in self.driver.page_source

    def testGmailInValidPassword(self):
        obj = GmailHelper(self.driver)
        obj.login("asdfdg")
        assert "Wrong password. Try again" in self.driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()