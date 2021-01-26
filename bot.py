from selenium import webdriver
import os
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InstagramBot:

    def __init__(self, username, password):
        """
        Initializes an instance of the InstgramBot class.
        Call the login method to authenticate a user with IG.

        Args:
        :param username:str: The Instagram username for a User
        :param password:str: The Instagram password for a User

        Attributes:
        driver:Selenium.webdriver.Chrome: The Chromedriver that is used to automate browser actions
        """
        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'

        # options = webdriver.ChromeOptions()  # Code To hide chrome browser while running the app
        # options.add_argument('headless')
        # boot up the browser for logging in to Instagram
        self.driver = webdriver.Chrome('./chromedriver.exe')  # ,options=options)
        self.login()

    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        time.sleep(2)  # Let the website full loading
        # if There is a Pop-Up windows to Accept cookies from Instagram on this browser:
        # self.driver.find_element_by_xpath("//button[contains(text(),'Accept')]").click()
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(5)
        # if There is a Pop-Up windows to turn on notification we will use this line:
        # self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()

    def nav_user(self, user):
        """
        Args:
              :param user:str: The username of the instagram user

        Navigate to the users page
        """
        self.driver.get('{}/{}/'.format(self.base_url, user))

    def follow_user(self, user):
        """
        Args:
            :param user:str: The username of the instagram user

        Follow a user
        """
        self.nav_user(user)
        self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0].click()

    def unfollow_user(self, user):
        """
        Args:
            :param user:str: The username of the instagram user

        unfollows a user
        """
        self.nav_user(user)
        self.driver.find_elements_by_xpath("//button[contains(@class, '_5f5mN    -fzfL     _6VtSN     yZn4P ')]")[
            0].click()
        self.driver.find_elements_by_xpath("//button[contains(text(), 'Unfollow')]")[0].click()

    def message(self, user, message):
        self.nav_user(user)
        self.driver.find_elements_by_xpath("//button[contains(text(), 'Message')]")[0].click()
        time.sleep(2)
        # if There is a Pop-Up windows to turn on notification we will use this line:
        try:
            self.driver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        except:
            self.driver.find_element_by_xpath("//textarea[contains(@placeholder,'Message...')]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//textarea[contains(@placeholder,'Message...')]").send_keys(message)
            self.driver.find_elements_by_xpath("//button[contains(text(), 'Send')]")[0].click()

    
    def messege_profile(self):
        users = open(r"D:\Python\InstagramBot\users.txt", "r")
        for user in users:
            user = user.strip('\n')
            self.message(user, 'Follow For Follow! '
                               'https://www.instagram.com/userName/')
            time.sleep(2)

    # Follow all the users that under following
    def follow_list_of_users(self, user):
        self.nav_user(user)
        self.driver.find_element_by_partial_link_text("followers").click()
        time.sleep(3)
        buttons = self.driver.find_elements_by_xpath("//button[contains(.,'Follow')]")
        for btn in buttons:
            # Use the Java script to click on follow because after the scroll down the buttons will be un clickeable
            # unless you go to it's location
            self.driver.execute_script("arguments[0].click();", btn)
            time.sleep(2)

   

if __name__ == '__main__':
    ig_bot = InstagramBot('your_username', 'your_password')
    # ig_bot.message('userName', 'hey, Follow Me!')
    # ig_bot.messege_profile()
    # ig_bot.follow_all('leomessi')
    # ig_bot.follow_list_of_users('leomessi')
