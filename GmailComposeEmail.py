from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import datetime
from GmailHelper import GmailHelper
import unittest

class GmailComposeEmail(unittest.TestCase):
    """To test composing a new email in Gmail"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        gmailHelper = GmailHelper(self.driver)
        gmailHelper.login()
        assert "Inbox" in self.driver.page_source
        self.driver.implicitly_wait(30)
        composeXpath = self.driver.find_element_by_xpath("//div[@gh='cm']")
        composeXpath.click()
        self.driver.implicitly_wait(30)
        emailTo = self.driver.find_element_by_name("to")  # Specify receiver of email
        emailTo.send_keys("ashugoeltesting@gmail.com")

    def testGmailComposeWithoutAnyContent(self):
        driver = self.driver
        sendButton = driver.find_element_by_xpath("//div[text()='Send']")
        sendButton.click()
        driver.implicitly_wait(15)
        alert = driver.switch_to.alert
        assert "Send this message without a subject or text in the body?" in alert.text
        alert.accept()

    def testGmailComposeWithContent(self):
        driver = self.driver
        emailSubjectBox = driver.find_element_by_name("subjectbox")
        dateTime = str(datetime.datetime.now())
        emailSubjectBox.send_keys("Test Email " + dateTime)
        emailContent = driver.find_element_by_xpath("//div[@aria-label='Message Body']")  # Content of the email
        emailContent.send_keys("Test Email Content!")
        sendButton = driver.find_element_by_xpath("//div[text()='Send']")
        sendButton.click()
        driver.implicitly_wait(20)
        try:
            emailSubject = driver.find_element_by_xpath("//span/b[text()='Test Email " + dateTime + "']")
        except NoSuchElementException:
            assert False

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()





