from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GmailHelper:
    """Utility class for logging into Gmail"""
    def __init__(self,driver):
        self.driver = driver

    def login(self,password="Testing@ID2001"):
        driver = self.driver
        driver.get(
            "https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier")
        assert "Gmail" in driver.title
        email_id = driver.find_element_by_name("Email")
        email_id.send_keys("ashugoeltesting")
        email_id.send_keys(Keys.RETURN)
        next_button = driver.find_element_by_id("next")
        next_button.submit()
        driver.implicitly_wait(30)
        user_password = driver.find_element_by_id("Passwd")
        user_password.send_keys(password)
        sign_in = driver.find_element_by_id("signIn")
        sign_in.submit()

    def logout(self):
        sign_out_profile = self.driver.find_element_by_xpath("//*[@id='gb']/div[1]/div[1]/div[2]/div[4]/div[1]/a/span")
        sign_out_profile.click()
        sign_out = self.driver.find_element_by_id("gb_71")
        sign_out.click()

