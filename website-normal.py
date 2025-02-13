## Website Normal Usage

# Create and activate a virtual environment:
# python3 -m venv venv
# source venv/bin/activate  (Mac/Linux)
# venv\Scripts\activate      (Windows)

# Install required dependencies:
# pip3 install selenium webdriver-manager

# Run the script:
# python3 website-normal.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Install and set up ChromeDriver automatically
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the target website
browser.get('https://www.erkankavas.com/')

# Wait for user input before closing
input('Press ENTER to close the automated browser')

# Close the browser
browser.quit()