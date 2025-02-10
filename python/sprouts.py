##############################################################################
# Author(s): Madelin A. (@madelinab)
# Created Date: 2/9/2025
# Description: Scrapes Sprout's website to get all the items they have available
# Revision:
#           2/9/2025 - @madelinab - imported selenium to scrape dynamic web pages
##############################################################################

import pandas as pd
from selenium import webdriver

fruit_website = 'https://shop.sprouts.com/store/sprouts/collections/n-produce-fruits'
path = '/Users/madelinarias/Documents/chromedriver-mac-arm64/chromedriver'
driver = webdriver.Chrome(path)
driver.get(fruit_website)
driver.quit()