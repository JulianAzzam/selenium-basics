# Importing Selenium
from selenium import webdriver
# Importing the time library
import time
from selenium.webdriver.common.by import By
# Importing Actions
from selenium.webdriver.common.action_chains import ActionChains

# Creating the browser instance
browser = webdriver.Chrome()
# Going to Loop's website
browser.get("https://loop.org.il")
# makes the program sleep for 3 to wait for the page to load
time.sleep(3)
# Fetching the OUR MAGIC button on Loop's website by it's XPath
button = browser.find_element(By.XPATH, "//span[normalize-space()='Our magic']")
# Clicks on the element
button.click()
# Waiting for page to load
time.sleep(3)
# Fetching the Loop Logo at the bottom on the page
logo_picture = browser.find_element(By.XPATH, "//img[@alt='text.jpg']")
# Creating an instance of ActionChains which allows us to perform actions against an element
actions = ActionChains(browser)
# Moving the screen to the element
actions.move_to_element(logo_picture).perform()
