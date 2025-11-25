from time import sleep
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os

# X API AUTH
from requests_oauthlib import OAuth1
import requests
API_KEY = os.getenv("X_API_KEY")
API_SECRET = os.getenv("X_API_SECRET")
ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("X_TOKEN_SECRET")
auth = OAuth1(API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
# END X API AUTH

SPEEDTEST_URL = "https://www.speedtest.net"
PROMISED_DOWN = 210.00
PROMISED_UP = 12.00
CHROME_DRIVER_PATH = "/Users/ben/Development/chromedriver"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.up = 0
        self.down = 0
        self.test_id = 0
        self.chrome_options = webdriver.ChromeOptions()
        # Keep Chrome browser open after program finishes? True/False
        self.chrome_options.add_experimental_option(name="detach", value=False)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def get_internet_speed(self): # Get current internet speed.
        self.driver.get(SPEEDTEST_URL)
        wait = WebDriverWait(self.driver,timeout=2)
        sleep(5)
        try:
            wait.until(lambda _ : self.driver.find_element(By.CSS_SELECTOR,".start-button a"))
        except TimeoutException:
            print("ERROR: The Go button did not load in the specified time or does not exist.")
        except NoSuchElementException:
            print("ERROR: The Go button was not found. Check the find_element ID.")

        start_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        start_button.click()

        test_wait = WebDriverWait(self.driver,timeout=60)
        try:
            if test_wait.until(lambda _ : self.driver.find_element(By.CSS_SELECTOR,".result-data > a").text.strip() != ""):
                result_id = self.driver.find_element(By.CSS_SELECTOR,".result-data > a").text.strip()
                download_speed = self.driver.find_element(By.CSS_SELECTOR,"span.download-speed").text.strip()
                upload_speed = self.driver.find_element(By.CSS_SELECTOR,"span.upload-speed").text.strip()

                self.up = float(upload_speed)
                self.down = float(download_speed)
                self.test_id = result_id

                result = [result_id,download_speed,upload_speed]

            else:
                result = "Result Data not found"

            return result

        except TimeoutException:
            return print("ERROR: The result did not load in the specified time or does not exist.")
        except NoSuchElementException:
            return print("ERROR: The result was not found. Check the find_element ID.")

    def tweet_at_provider(self):
        # X now requires API to create posts. Cannot use Selenium to simulate human-like interaction.
        tweet_url = "https://api.x.com/2/tweets"
        payload = {
            "text": f"Hey ISP! Why is my internet speed {self.down}🔻/{self.up}🔺 "
                    f"when I am paying for {PROMISED_DOWN}🔻/{PROMISED_UP}🔺? "
                    f"Link: https://www.speedtest.net/result/{self.test_id}."
        }
        response = requests.post(tweet_url, json=payload, auth=auth)
        print(response.json())

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

if bot.up < PROMISED_UP and bot.down < PROMISED_DOWN:
    bot.tweet_at_provider()