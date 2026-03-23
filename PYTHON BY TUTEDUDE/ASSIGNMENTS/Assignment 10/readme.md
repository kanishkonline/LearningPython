# Price Tracker Application (Web Scraping)

## Objective

In this assignment, I created a Python program that tracks the price of a product from a website using web scraping.

## Libraries Used

* requests
* BeautifulSoup (bs4)

## How It Works

* The program sends a request to a product webpage
* It reads the HTML content of the page
* Then it finds the price using a specific HTML tag
* The price is cleaned and converted into a number
* Finally, it compares the price with a target value

## How to Run

1. Install required libraries:
   pip install requests beautifulsoup4

2. Run the program:
   python price_tracker_app.py

## Output

The program prints:

* Current product price
* Message if price is lower or higher than target

## Conclusion

This project helped me understand how web scraping works using Python and how to extract useful data from websites.


## Author
Kanishk Singh