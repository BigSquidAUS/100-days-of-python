from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach",value=True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com.au/TP-Link-AX3000-Wi-Fi-Range-Extender/dp/B0BB79NDS2/")
price_dollars = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text

print(f"The price is ${price_dollars}.{price_cents}")



#driver.close() # Closes Tab.
#driver.quit() # Closes entire browser.