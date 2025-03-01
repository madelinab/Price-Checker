##############################################################################
# Author(s): Madelin A. (@madelinab)
# Created Date: 2/9/2025
# Description: Scrapes Sprout's website to get all the items they have available
# Revision:
#           2/09/2025 - @madelinab - imported selenium to scrape dynamic web pages
#           2/16/2025 - @madelinab - installed chromedriver through terminal using Homebrew
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
# - Search for each category of item
# - Get the contents of each aisle
# - Store contents in a database location
#driver = webdriver.Chrome('/opt/homebrew/bin/chromedriver')


try:
    options = Options()
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--verbose")
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(180)  # Set a higher page load timeout

    categories = ['https://shop.sprouts.com/store/sprouts/collections/n-produce', 
                  'https://shop.sprouts.com/store/sprouts/collections/n-deli', 
                  'https://shop.sprouts.com/store/sprouts/collections/n-bakery', 
                  'https://shop.sprouts.com/store/sprouts/collections/n-bulk', 
                  'https://shop.sprouts.com/store/sprouts/collections/n-dairy', 
                  'https://shop.sprouts.com/store/sprouts/collections/n-meat-seafood', 
                  'https://shop.sprouts.com/store/sprouts/collections/n-grocery-aisles', 
                  'https://shop.sprouts.com/store/sprouts/collections/n-frozen'
                  ]
    driver.get(categories[0]) #test if it works on a different page

    # Wait for the delivery/pickup pop-up to appear
    wait = WebDriverWait(driver, 20)  # Wait for up to 20 seconds

    confirm_button = wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Confirm')]")) # the confirm button is in a <span> tag

    )
    
    confirm_button.click()
    print('Confirm button clicked!')

    time.sleep(10)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    print(soup.prettify())


except Exception as e:
    print(f"Error: {e}")
    #print(driver.page_source)  # Prints the HTML of the current page
    #print(driver.current_url)   # Prints the current URL of the page

finally:
    time.sleep(5)  # keeps browser open for a few seconds before quitting
    driver.quit()