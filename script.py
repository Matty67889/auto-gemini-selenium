import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# navigate to website
driver.get("https://gemini.google.com/")
time.sleep(5)
driver.close()