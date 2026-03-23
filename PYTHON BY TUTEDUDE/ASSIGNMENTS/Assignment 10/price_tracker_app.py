# Price Tracker Application (Web Scraping)

import requests
from bs4 import BeautifulSoup

# product URL (I am using a sample website)
url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

# target price (if price goes below this, we show message)
target_price = 50

try:
    # sending request to website
    response = requests.get(url)

    # checking if request is successful
    if response.status_code == 200:

        # parsing HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # finding price from HTML
        price_tag = soup.find("p", class_="price_color")

        # getting text and cleaning it
        price_text = price_tag.text
        clean_price = price_text.replace("£", "").replace("Â", "").strip()

        # converting to float
        price = float(clean_price)

        print("Current Price:", price)

        # comparing price
        if price < target_price:
            print("Price dropped! You can buy now.")
        else:
            print("Price is still high.")

    else:
        print("Failed to fetch page")

except Exception as e:
    print("Error:", e)