#!/usr/bin/env python
from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory

class Homepage(PageFactory):
    """
    Class used to manage the Homepage.

    Attributes:
        driver (webdriver): The webdriver to use
        locators (dictionary): The page elements
    """

    locators = {
                "accept_cookies_button": ("ID", "L2AGLb"),
    }


    def __init__(self, driver):
        """
        Initialize the Homepage object.

        Args:
            driver (webdriver): The webdriver to use
        """
        self.driver = driver


    def accept_cookies(self):
        """
        Clicks on the accept_cookies_button.

        """
        self.accept_cookies_button.click()


    def get_wikipedia_link(self):
        """
        Gets the link to go to the Wikipedia entry

        Returns: The Wikipedia link
        """
        wikipedia_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Wikipedia').get_attribute("href")
        return wikipedia_link
