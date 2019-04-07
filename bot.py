from selenium import webdriver
import time


class boTweet(object):
    """
    Twitter bot for sending automatic tweets
    """

    def __init__(self):
        self.username = input("Please provide a username: ")
        self.password = input("Please provide a password: ")
        # self.tweet = input("Please enter your tweet: ")  # you can directly type your tweet or
        self.tweet = self.text_reader()                    # you can provide a txt file
        self.__str__()
        self.connect()
        self.logout()


    def __str__(self):
        print("Hello ", self.username)
        time.sleep(1)
        print("Sit tight while i am getting things ready for you")
        time.sleep(1)

    def text_reader(self):
        self.filename = input("Please provide a filename: ")
        with open(self.filename, "r+", encoding="UTF-8") as file:
            f = file.read(140)  # Don't exceed the tweet limit
            return f

    def connect(self):
        self.driver = webdriver.Firefox()
        time.sleep(1)
        self.driver.get("https://www.twitter.com")
        time.sleep(1)
        username = self.driver.find_element_by_name("session[username_or_email]").send_keys(self.username)
        time.sleep(1)
        password = self.driver.find_element_by_name("session[password]").send_keys(self.password)
        time.sleep(1)
        dologin = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[1]/form/input[1]").click()
        time.sleep(1)
        your_message = self.driver.find_element_by_name("tweet").send_keys(self.tweet)
        time.sleep(1)
        send_tweet = self.driver.find_element_by_css_selector("form.tweet-form:nth-child(2) > div:nth-child(3) > div:nth-child(2) > button:nth-child(2) > span:nth-child(1)").click()
        time.sleep(1)


    def logout(self):
        profile_pic = self.driver.find_element_by_id("user-dropdown-toggle").click()
        time.sleep(1)
        do_log_out = self.driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div/div/div[3]/ul/li[1]/div/ul/li[13]/button").click()
        time.sleep(2)
        self.driver.quit()



