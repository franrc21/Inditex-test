#!/usr/bin/env python

#imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.homepage import Homepage
from pages.wikipedia import Wikipedia


##Constants and variables
GOOGLE_URL = "https://google.es/search?q="
KEYWORD = "automatización"
TEXT_TO_FIND = 'primer proceso'
driver = webdriver.Firefox()
screenshot_name = 'screenshot.png'
partial_screenshot_name = 'paragraph_screenshot.png'


##Program execution
print("Finding \"" + KEYWORD + "\" in Google...\n")
driver.get(GOOGLE_URL + KEYWORD)
google = Homepage(driver)
google.accept_cookies()

print("Selecting the Wikipedia link...\n")
wikipedia_link = google.get_wikipedia_link()
driver.get(wikipedia_link)
wikipedia = Wikipedia(driver)

print("Checking in which year the first automatic process took place...")
paragraph = wikipedia.find_paragraph_by_text(TEXT_TO_FIND)
print(paragraph.text)

print("\nTaking a screenshot of the Wikipedia's page...")
wikipedia.screenshot(screenshot_name)

print("\nTaking a screenshot of the selected paragraph...")
wikipedia.partial_screenshot(TEXT_TO_FIND, partial_screenshot_name)

driver.close()