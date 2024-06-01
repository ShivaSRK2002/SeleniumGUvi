import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

# Set the path for the ChromeDriver
paths = r"C:\Users\shiva\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)

# Set Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Keep the browser open after the script finishes

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open the target webpage
driver.get("https://www.saucedemo.com/")
driver.maximize_window()  # Maximize the browser window

# Locate the username input field and enter the username
userName = driver.find_element(By.ID, "user-name")
userName.click()  # Click on the username field
time.sleep(2)  # Wait for 2 seconds
userName.send_keys("standard_user")  # Type the username

# Locate the password input field and enter the password
password = driver.find_element(By.ID, "password")
password.click()  # Click on the password field
time.sleep(2)  # Wait for 2 seconds
password.send_keys("secret_sauce")  # Type the password

# Locate the login button and click it
login = driver.find_element(By.ID, "login-button")
login.click()  # Click the login button

# Print the title of the current webpage
print(driver.title)

# Print the current URL of the webpage
print(driver.current_url)

# Extract the entire page source (HTML content)
page_content = driver.page_source

# Save the extracted content to a text file
with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(page_content)

# Close the browser
driver.close()
