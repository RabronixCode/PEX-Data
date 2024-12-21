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

# First always delete all files from the download_dir folder
for filename in os.listdir(download_dir):
    file_path = os.path.join(download_dir, filename)
    try:
        if os.path.isfile(file_path):  # Check if it's a file
            os.remove(file_path)  # Delete the file
            print(f"Deleted: {file_path}")
    except Exception as e:
        print(f"Failed to delete {file_path}: {e}")

# Click on the link - then wait a bit
for i, button in enumerate(downloads):
    button.click()
    time.sleep(5)


# Rename downloaded files
new_file_names = [f"file_{i+1}.xls" for i in range(len(downloads))]
for i, filename in enumerate(os.listdir(download_dir)):
    old_path = os.path.join(download_dir, filename)
    new_path = os.path.join(download_dir, new_file_names[i])
    if os.path.isfile(old_path):
        shutil.move(old_path, new_path)
        print(f"Renamed: {old_path} to {new_path}")

