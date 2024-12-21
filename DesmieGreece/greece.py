from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

# Automatic downloads
download_dir = "C:\Users\User\Desktop\Python\MVM\PEX\DesmieGreece" # Download directory

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