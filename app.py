from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Set up Selenium options to include a User-Agent
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
options.add_argument("--window-size=1920,1080")  # Set a default window size

# Set up the Selenium driver (in this case, I'm using Chrome)
driver = webdriver.Chrome(options=options)

# Navigate to the URL
URL = "https://cars.ksl.com/search/"
driver.get(URL)
driver.maximize_window()

# Wait for the page to fully load (adjust the time and conditions as needed)
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".listingGrid"))
    )
finally:
    # Once the page has loaded, you can parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Find and print car details (again, adjust the selectors as necessary)
    for car_ad in soup.select('.listing'):
        title = car_ad.select_one('.listing-title')
        price = car_ad.select_one('.eaOVFJ')
        #phone = car_ad.select_one('.Listing__PhoneNumber-sc-1v5k5vh-6')
        #print('phone')
        #print(phone)
            
        link  = ""
        if title:
            link = title.get('href')
        if title and price:
            print(f"Title: {title.get_text(strip=True)}, Price: {price.get_text(strip=True)}, Link: {link}")

    # Save the page source to 'index.html'
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(driver.page_source)

    # Close the browser
    driver.quit()
