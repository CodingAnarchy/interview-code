import requests

r = requests.get('https://api.gdax.com/products/BTC-USD/book?level=3')
asks = r.json()['asks']

to_buy = input("How much bitcoin do you want to buy? ")

bought = 0.0
ask_idx = 0
total_price = 0.0
while bought < to_buy:
    try:
        next_ask = asks[ask_idx]
    except IndexError:
        print "Not enough to be sold."
        exit()
        
    price = float(next_ask[0])
    amt = float(next_ask[1])
    rem = to_buy - bought
    if amt >= rem:
        total_price += rem * price
        bought = to_buy
    else:
        total_price += amt * price
        bought += amt
    ask_idx += 1

print total_price
