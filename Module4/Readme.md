# Module-4  Assessment
1.Write a python script using selenium for automating the process of searching for a specific product on Amazon and extracting information about the first few results. Specifically, you need to:
1. Open Amazon's homepage.
2. Search for a specific product (e.g., "laptop").
3. Extract information about the first 5 search results, including:
Product title
Product price (if available)
Product rating (if available)
Number of reviews (if available)
4. Print this information in a structured format.

```python
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
```

2. Create a new data in any of the open source server  modify them and delete them using Postman.
   > CREATE
   > ![postman1](https://github.com/user-attachments/assets/20c17716-10fe-4b01-a965-6aa8af3b6bb7)

   >GET
   >![postman2](https://github.com/user-attachments/assets/477d8fd9-7c83-4c58-bea5-0f80cdf14a07)
   
   >PUT
   >![postman3](https://github.com/user-attachments/assets/90571bb9-d33d-4af8-b272-2376ffaff890)

   >DELETE
   >![postman4](https://github.com/user-attachments/assets/965218ba-ae3a-450c-a93c-989a4cdbbcfe)
   
