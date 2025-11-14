import os
from operator import contains
from time import sleep

from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

# Credentials (Fake...)
ACCOUNT_EMAIL = "fakeemail@what.com"
ACCOUNT_PASSWORD = "piddle"
GYM_URL = "https://appbrewery.github.io/gym/"

# Keep Chrome browser open after program finishes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach",value=True)

# Give Selenium its own user profile.
user_data_dir = os.path.join(os.getcwd(), "chrome_profile") # Create a directory in the current working directory called "chrome_profile".
chrome_options.add_argument(f"--user-data-dir={user_data_dir}") # Store a profile in the new directory.

# Create the web driver that uses all the chrome_options set above.
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the gym URL
driver.get(GYM_URL)

# Click the login button, fill in your details, submit.
login_button = driver.find_element(By.ID,"login-button")
login_button.click()

# Wait for next page to load.
wait = WebDriverWait(driver, timeout=2)
try:
    wait.until(lambda _ : driver.find_element(By.ID,"login-form").is_displayed() )
    print("SUCCESS: Login form found - continuing...")
except TimeoutException:
    print("ERROR: The login form did not load in the specified time or does not exist.")
except NoSuchElementException:
    print("ERROR: The login form was not found. Check the find_element ID.")

# Fill in your login details.
email_field = driver.find_element(By.ID,"email-input")
password_field = driver.find_element(By.ID, "password-input")
submit_button = driver.find_element(By.ID, "submit-button")

email_field.send_keys(ACCOUNT_EMAIL)
password_field.send_keys(ACCOUNT_PASSWORD)
submit_button.click()

try:
    wait.until(presence_of_element_located((By.ID,"welcome-message")))
    print("SUCCESS: Logged in.")
except TimeoutException:
    print("ERROR: Log in timed out or failed.")

# Start the counters | Step 5: Add counters
classes_booked = 0
waitlists_joined = 0
already_booked = 0
tues_6pm_classes_processed = 0

# Book upcoming Tuesday & Thursday Classes
class_cards = driver.find_elements(By.CSS_SELECTOR,"[id^=class-card-") # Get ALL of the divs with an ID containing class-card-
for class_card in class_cards:
    parent = class_card.find_element(By.XPATH,"..") # Get reference to the parent of the current class_card.
    day_title = parent.find_element(By.TAG_NAME,"h2").text
    if "Tue" in day_title or "Thu" in day_title:
        class_name = class_card.find_element(By.CSS_SELECTOR,"[id^=class-name-]").text
        class_time = class_card.find_element(By.CSS_SELECTOR,"[id^=class-time-]").text
        if "6:00 PM" in class_time:
            button = class_card.find_element(By.TAG_NAME,"button")
            if button.text == "Booked":
                print(f"Already booked")
                already_booked += 1
            elif button.text == "Waitlisted":
                print(f"Already on waitlist")
                already_booked += 1
            elif button.text == "Book Class":
                button.click()
                classes_booked += 1
                print(f"Successfully Booked!")
            elif button.text == "Join Waitlist":
                button.click()
                waitlists_joined += 1
                print(f"Joined Wait List!")

print("--- BOOKING SUMMARY ---")
print(f"Classes booked: {classes_booked}")
print(f"Waitlists joined: {waitlists_joined}")
print(f"Already booked or waitlisted: {already_booked}")
print(f"Total Tuesday 6pm Classes Processed: {tues_6pm_classes_processed}")

total_booked = classes_booked + waitlists_joined + already_booked

driver.get(f"{GYM_URL}/my-bookings/")
sleep(0.5)

booked_classes = driver.find_elements(By.CSS_SELECTOR,"[id^=booking-card-booking]")
waitlisted_classes = driver.find_elements(By.CSS_SELECTOR,"[id^=waitlist-card-waitlist")

classes_actual = len(booked_classes) + len(waitlisted_classes)

if  classes_actual == total_booked:
    print(f"SUCCESS: Expected: {total_booked} bookings | Actual: There are {classes_actual} bookings!")
else:
    print(f"Actual booked classes amount does not match. There has been an error.")