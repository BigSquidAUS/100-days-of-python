from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach",value=True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

the_target = driver.find_element(By.XPATH,value='//*[@id="articlecount"]/ul/li[2]/a[1]')
print(the_target.text)

the_target.click()