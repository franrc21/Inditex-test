#!/usr/bin/env python
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory

class Wikipedia(PageFactory):
    """
    Class used to manage the Wikipedia page.

    Attributes:
        driver (webdriver): The webdriver to use
        locators (dictionary): The page elements
    """

    locators = {
                "paragraph_to_print": (None, None)
    }


    def __init__(self, driver):
        """
        Initialize the Wikipedia object.

        Args:
            driver (webdriver): The webdriver to use
        """
        self.driver = driver


    def find_paragraph_by_text(self, text_to_find):
        """
        Finds the paragraph that contains "text_to_find"

        Args:
            text_to_find (string): The text that the paragraph must contain

        Returns: The found paragraph
        """
        pattern = '//p[contains(.,"' + text_to_find + '")]'
        self.locators["paragraph_to_print"] = ('Xpath', pattern)
        return self.paragraph_to_print


    def partial_screenshot(self, text_to_find, screenshot_name):
        """
        Find the paragraph that contains a text and take a screenshot of the paragraph.

        Args:
            text_to_find (string): The text that the paragraph must contain
            screenshot_name (string): The name of the screenshot
        """
        p = self.driver.find_element(By.XPATH, '//p[contains(.,"' + text_to_find + '")]')
        p.screenshot(screenshot_name)


    def screenshot(self, screenshot_name):
        """
        Take a screenshot of the Wikipedia's page

        Args:
            screenshot_name (string): The name of the screenshot
        """
        self.driver.save_screenshot(screenshot_name)