import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time 

def scrape_website(website):
    print("Launching chrome browser....")

    chrome_driver_path = "./chromedriver.exe"  
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Run Chrome in headless mode (optional)
    # options.add_argument("--disable-gpu")  # Disable GPU acceleration (optional)
    # options.add_argument("--no-sandbox")  # Bypass OS security model (optional)

    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
      

        driver.get(website)
        print("Page loaded..")
        html = driver.page_source
        time.sleep(50)     

        return html
    finally:
        driver.quit()