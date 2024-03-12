# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Add LinkedIn credentials here
linkedin_username = "manishkoladiya08@gmail.com"
linkedin_password = "Assignment3@@@"

# Navigating to the LinkedIn sign-in page
driver.get("https://www.linkedin.com/login")
time.sleep(3)

# Finding the email field and entering email
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(linkedin_username)

# Finding the password field and entering password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(linkedin_password)

# Submitting the login information
password_field.submit()
time.sleep(3)

# Navigating to the 'Jobs' page
jobs_tab = driver.find_element(By.LINK_TEXT, "Jobs")
jobs_tab.click()
time.sleep(5)

# Navigating to the 'Notifications' page
Notifications_tab = driver.find_element(By.LINK_TEXT, "Notifications")
Notifications_tab.click()
time.sleep(8)

# Opening the 'Messaging' panel
messaging_icon = driver.find_element(By.LINK_TEXT, "Messaging")
messaging_icon.click()
time.sleep(3)

# Opening the 'My Network' panel
messaging_icon = driver.find_element(By.LINK_TEXT, "My Network")
messaging_icon.click()
time.sleep(3)

# Closing the webdriver
driver.quit()
