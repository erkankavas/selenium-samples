## Speed Test Usage

# Create and activate a virtual environment:
# python3 -m venv venv
# source venv/bin/activate  (Mac/Linux)
# venv\Scripts\activate      (Windows)

# Install required dependencies:
# pip3 install selenium webdriver-manager

# Run the script:
# python3 speed-test.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome with options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Optional: Runs in background

# Start the browser
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open Fast.com
browser.get("https://fast.com")

# Wait for speed test to complete
time.sleep(15)  # Adjust if needed

# Get the speed result
speed = browser.find_element(By.CLASS_NAME, "speed-results-container").text

print(f"Download Speed: {speed} Mbps")

# Close the browser
browser.quit()