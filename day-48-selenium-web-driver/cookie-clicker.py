import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep,time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach",value=True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

#Select language screen
sleep(2)
lang_select = driver.find_element(By.ID,"langSelect-EN")
lang_select.click()

sleep(3)
cookie_button = driver.find_element(By.ID, value="bigCookie")

def convert_to_digits_only(the_string: str) -> int:
    """Removes all non-digit characters from a string and returns the string as an int"""
    digits = re.sub(pattern='[^0-9]',repl='',string=the_string)
    return int(digits)

def click_cookie():
    start_time = time()
    while (start_time + 6) > time(): # Start clicking the cookie for x seconds then..
        cookie_button.click()

def buy_items():
    try:
        #Wait up to 1 second to find the element below
        item = WebDriverWait(driver,.2).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,'#upgrades .enabled'))
        )
        item.click()
        print("Item bought")

    except TimeoutException:
        # Element not found within 1 second, just move on
        print("No item available, moving on.")

    print("Item check complete - now checking for upgrades.")

def buy_upgrades():
    available_upgrades = get_available_upgrades()
    best_upgrade = None
    max_cost = 0

    if len(available_upgrades) > 0: #If available_upgrades dict is not empty then click on the most expensive upgrade.
        for upgrade in available_upgrades.values():
            if upgrade["cost"] > max_cost:
                best_upgrade = upgrade["upgrade"]

        best_upgrade.click()
        buy_upgrades()
    else:
        print("Can't afford anymore upgrades.")

def get_available_upgrades() -> dict:
    print("Checking what upgrades are available to you...")
    upgrades_list = driver.find_elements(By.CSS_SELECTOR,"#products .enabled")
    available_upgrades = {}
    available_upgrades.clear()

    for i in range(0,len(upgrades_list)):
        the_upgrade = upgrades_list[i]
        the_cost_text = upgrades_list[i].find_element(By.CLASS_NAME,"price").text.strip()
        the_cost = convert_to_digits_only(the_cost_text)
        sleep(0.2)

        if the_cost <= get_cookie_amount():
            available_upgrades[i] = {
                "upgrade":the_upgrade,
                "cost": the_cost
            }
        else:
            print("You cannot afford any upgrades yet.")
            available_upgrades = {}

    return available_upgrades

def get_cookie_amount() -> int:
    cookie_amount = driver.find_element(By.ID,"cookies").text
    cookie_amount = convert_to_digits_only(cookie_amount.split()[0])
    return cookie_amount

def main_loop():
    while True:
        click_cookie()
        buy_items()
        buy_upgrades()
        sleep(0.1)

try:
    main_loop()
except Exception as e:
    print("Error:", e)