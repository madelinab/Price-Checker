##############################################################################
# Author(s): Madelin A. (@madelinab)
# Created Date: 2/9/2025
# Description: Scrapes Sprout's website to get all the items they have available
# Revision:
#           2/9/2025 - @madelinab - imported selenium to scrape dynamic web pages
##############################################################################

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

#TODO: 
# - Figure out how to get sprouts loaded faster
# - Search for each aisle: fruit, vegetables, meat, dairy, grains, starches, supplements
# - Get the contents of each aisle
# - Store contents in a database location
driver = webdriver.Chrome()

try:
    # open sprouts page
    website = 'https://shop.sprouts.com/store/sprouts/storefront'

    driver.get(website)

    time.sleep(3)  # wait for page to load

    # when the page opens, it'll ask if you want in-store pickup or delivery,
    # we want selenium to just click the 'confirm' button
    confirm_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Confirm')]").click()

    time.sleep(5)  # wait for progress

    # search for a category
    search_box = driver.find_element(By.XPATH, "//input[contains(text(), 'Search Sprouts Farmers Market')]").click()
    search_box.send_keys('vegetables') # the aisle it needs to search for
    search_box.send_keys(Keys.RETURN) # hit the 'enter' key
    
    time.sleep(10) # puase to let the site load

except Exception as e:
    print(f"Error: {e}")

finally:
    time.sleep(5)  # keeps browser open for a few seconds before quitting
    driver.quit()