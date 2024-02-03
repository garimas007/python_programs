"""
Accessing variable from different scope
"""

def calculate_total(prices):
    total = sum(prices)
    print(total)

item_prices = [10,100,300]
calculate_total(item_prices)
#print(total)