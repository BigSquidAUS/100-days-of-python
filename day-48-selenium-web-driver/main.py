from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach",value=True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

event_dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget div .menu li time")
event_titles = driver.find_elements(By.CSS_SELECTOR, value=".event-widget div .menu li a")

events = {}

for i in range(0,len(event_dates)):
    events[i] = {
        "time": event_dates[i].text,
        "name": event_titles[i].text
    }

print(events)
