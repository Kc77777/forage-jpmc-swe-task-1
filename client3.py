import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server requests
N = 500

def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    
    # Calculate the correct price using the formula (bid_price + ask_price) / 2
    price = (bid_price + ask_price) / 2
    
    return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    # Check if price_b is zero to avoid division by zero
    if price_b == 0:
        return 0  # or any other appropriate value or handling
    # Calculate the ratio between price_a and price_b
    return price_a / price_b

# Main
if __name__ == "__main__":
    # Initialize a dictionary to store stock prices
    prices = {}
    
    # Query the price once every N seconds.
    for _ in range(N):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        # Iterate through quotes and store prices
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            
            # Store the price in the prices dictionary using the stock name as the key
            prices[stock] = price

        # Check if both 'ABC' and 'DEF' prices are available
        if 'ABC' in prices and 'DEF' in prices:
            # Calculate and print the ratio using the stored prices
            ratio = getRatio(prices['ABC'], prices['DEF'])
            print("Ratio (ABC/DEF): %s" % ratio)
