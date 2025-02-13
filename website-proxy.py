## Website Proxy Usage

# Create and activate a virtual environment:
# python3 -m venv venv
# source venv/bin/activate  (Mac/Linux)
# venv\Scripts\activate      (Windows)

# Install required dependencies:
# pip3 install webdriver-manager seleniumwire

# solution (if not work)
# pip3 install --upgrade setuptools
# pip3 install blinker==1.7.0    

# Run the script:
# python3 website-proxy.py

from seleniumwire import webdriver  # Use SeleniumWire instead of Selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Proxy credentials
PROXY_HOST = "xxx.xxxxxx.com"  # Change this
PROXY_PORT = "XXXXX"  # Change this
PROXY_USERNAME = "username"  # Change this
PROXY_PASSWORD = "password"  # Change this


# Selenium Wire Options (for proxy authentication)
seleniumwire_options = {
    'proxy': {
        'http': f'http://{PROXY_USERNAME}:{PROXY_PASSWORD}@{PROXY_HOST}:{PROXY_PORT}',
        'https': f'https://{PROXY_USERNAME}:{PROXY_PASSWORD}@{PROXY_HOST}:{PROXY_PORT}',
        'no_proxy': 'localhost,127.0.0.1'  # Bypass local addresses
    }
}

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options, seleniumwire_options=seleniumwire_options)

# Open the target website
driver.get("https://www.erkankavas.com")

input('Press ENTER to close the automated browser')

# Close the browser
driver.quit()
