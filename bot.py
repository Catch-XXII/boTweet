import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class BOTweet(object):
    _URL = "https://x.com/"
    """
    Twitter bot for sending automatic tweets
    """

    def __init__(self, username, password, tweet):
        self.username = username
        self.password = password
        self.tweet = tweet
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
        self.__str__()
        self.connect()
        self.logout()

    def __str__(self):
        print("Hello ", self.username)
        time.sleep(1)
        print("Sit tight while i am getting things ready for you")
        time.sleep(1)

    def connect(self):
        time.sleep(1)
        self.driver.get(self._URL)
        time.sleep(1)

        self.driver.find_element(
            By.XPATH,
            "(//div[@class='css-146c3p1 r-bcqeeo r-qvutc0 r-37j5jr r-q4m81j r-a023e6 r-rjixqe r-b88u0q r-1awozwy r-6koalj r-18u37iz r-16y2uox r-1777fci'])[3]",
        ).click()

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='text']").send_keys(
            self.username
        )
        time.sleep(1)
        self.driver.find_element(By.NAME, "session[password]").send_keys(self.password)
        time.sleep(1)
        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[1]/form/input[1]"
        ).click()
        time.sleep(1)
        self.driver.find_element(By.NAME, "tweet").send_keys(self.tweet)
        time.sleep(1)
        self.driver.find_element(
            By.CSS_SELECTOR,
            "form.tweet-form:nth-child(2) > div:nth-child(3) > "
            "div:nth-child(2) > button:nth-child(2) > "
            "span:nth-child(1)",
        ).click()
        time.sleep(1)

    def logout(self):
        self.driver.find_element(By.ID, "user-dropdown-toggle").click()
        time.sleep(1)
        self.driver.find_element(
            By.XPATH,
            "/html/body/div[2]/div[1]/div[3]/div/div/div[3]/ul/li[1]/div/ul/li[13]/button",
        ).click()
        time.sleep(2)
        self.driver.quit()


if __name__ == "__main__":
    x = BOTweet("trump", "123456", "fuck you!")
