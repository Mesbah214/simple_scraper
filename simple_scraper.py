# File: simple_scraper.py
#       A simple program to monitor the price of a specific product at amazon.com and notify the user
#       if the price goes down by creating a text file at the user specified path.
# by: Mesbah Uddin


# importing modules which are necessary for this project
import requests
from bs4 import BeautifulSoup
import time

# setting the target url under url variable
url = "https://www.bestbuy.ca/en-ca/product/apple-macbook-pro-2020-w-touch-bar-13-3-space-grey-intel-i5-1-4ghz-256gb-ssd-8gb-ram-en/14627724"

# setting header to tell the server that we are not a robot
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537."}

# sending requests to the server to get the HTML
r = requests.get(url, headers=headers)

# parsing the retrived HTML with BeautifulSoup
soup = BeautifulSoup(r.content, "html.parser")

# extracting name of the product
title = soup.find(class_="productName_19xJx").text.strip()

# extracting the price of the product
price_str = soup.find(class_="price_FHDfG large_3aP7Z").text

# striping the dollar sign and converting the string to float
conv_pri = float(price_str.strip('$').replace(',', '.'))*1000

while True:
    # setting the boolean
    if conv_pri <= 1400:
        print("the price went down!!")

    # resting period after checking the price once
    time.sleep(14400)
