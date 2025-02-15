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

#TODO: 
# - Figure out how to get sprouts loaded faster
# - Search for each aisle: fruit, vegetables, meat, dairy, grains, starches, supplements
# - Get the contents of each aisle
# - Store contents in a database location
fruit_website = 'https://shop.sprouts.com/'
driver = webdriver.Chrome()
driver.get(fruit_website)
driver.quit()