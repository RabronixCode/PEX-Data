import os
import shutil
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By

# Automatic downloads
download_dir = "C:\\Users\\User\\Desktop\\Python\\MVM\\PEX\\DesmieGreece\\Files" # Download directory

chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": download_dir,  # Default dir
    "download.prompt_for_download": False,       # No prompt for download
    "download.directory_upgrade": True,          # Auto overwriting
    "safebrowsing.enabled": True                 # Safe browsing
})

# Set up WebDriver
service = Service('C:\\Users\\User\\Desktop\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

wait = WebDriverWait(driver, 20)

# Open the webpage
driver.get("https://www.enexgroup.gr/web/guest/markets-publications-el-day-ahead-market")  # Url of the website


# Cookies popup
cookie_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
cookie_button.click()


downloads = driver.find_elements(By.XPATH, f'//*[@class="portlet-body"]//a[contains(., "ResultsSummary")]') # Elements do be clicked/downloaded
#for d in downloads:
#    print(d.text)

