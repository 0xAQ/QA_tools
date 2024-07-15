import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#set webdriver 
os.environ['PATH'] += ":/home/aaquil/chromedriver-linux64"
driver = webdriver.Chrome()

#open Amazon.in
driver.get("https://amazon.in")

#seacrh laptop
search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
search_bar.send_keys("laptop")
search_bar.send_keys(Keys.RETURN)

# fetch details of the top 5 results
results = driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")[:5]
for idx, result in enumerate(results):
    try:
        title = result.find_element(By.CSS_SELECTOR, "h2 .a-link-normal").text
    except:
        title = "N/A"
    
    try:
        price = result.find_element(By.CSS_SELECTOR, ".a-price-whole").text
        price = f"₹ {price}"
    except:
        price = "N/A"
    
    try:
        rating = result.find_element(By.CSS_SELECTOR, ".a-icon-alt").get_attribute("innerHTML")
    except:
        rating = "N/A"
    
    try:
        reviews = result.find_element(By.CSS_SELECTOR, ".s-link-style .a-size-base").text
    except:
        reviews = "N/A"

    print(f"Result {idx+1}:")
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Rating: {rating}")
    print(f"Number of Reviews: {reviews}")
    print("="*40)

# Close the browser
driver.quit()
