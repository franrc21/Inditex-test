#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

print("Finding \"automatización\" in Google...\n")
keyword = "automatización"
driver.get("https://google.es/search?q="+keyword)
driver.find_element("id","L2AGLb").click()  #Accept cookies in Google

print("Selecting the Wikipedia link...\n")
wikipedia = driver.find_element(By.PARTIAL_LINK_TEXT, 'Wikipedia').get_attribute("href")
driver.get(wikipedia)

print("Checking in which year the first automatic process took place...")
elements = driver.find_elements(By.TAG_NAME, 'p')
for e in elements:
    text = e.text
    if 'primer proceso' in text:
        print(text)

print("\nTaking a screenshot of the Wikipedia's page...")
driver.save_screenshot('screenshot.png')
driver.close()